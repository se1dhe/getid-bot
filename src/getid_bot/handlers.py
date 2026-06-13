from __future__ import annotations

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command, CommandStart
from aiogram.types import CallbackQuery, Chat, Message, MessageOriginChannel, MessageOriginChat

from .formatters import (
    compact_json,
    format_chat,
    format_chat_lookup,
    format_contact_lookup,
    format_diagnostics,
    format_support_card,
    format_user,
    preformatted,
)
from .help_texts import (
    CHAT_ID_MENU,
    CONTACT_HELP,
    DIAGNOSTICS_MENU,
    HELP_OVERVIEW,
    HELP_TEXTS,
    MAIN_MENU_TEXT,
    RAW_FULL_WARNING,
    RAW_MENU,
)
from .keyboards import back_to_menu_keyboard, main_menu_keyboard, start_keyboard
from .observability import log_message_event
from .redaction import redact

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    log_message_event(message, "command", command="start")
    if message.from_user is None:
        await message.answer("Telegram did not include user data in this update.")
        return
    await message.answer(MAIN_MENU_TEXT, reply_markup=start_keyboard())


@router.callback_query(F.data == "menu:my_id")
async def handle_menu_my_id(callback: CallbackQuery) -> None:
    if callback.from_user is None or callback.message is None:
        await callback.answer("User data is unavailable.")
        return
    await callback.message.edit_text(
        format_user(callback.from_user),
        reply_markup=back_to_menu_keyboard(),
    )
    await callback.answer()


@router.callback_query(F.data == "menu:home")
async def handle_menu_home(callback: CallbackQuery) -> None:
    if callback.message is not None:
        await callback.message.edit_text(MAIN_MENU_TEXT, reply_markup=main_menu_keyboard())
    await callback.answer()


@router.callback_query(F.data == "menu:help")
async def handle_menu_help(callback: CallbackQuery) -> None:
    if callback.message is not None:
        await callback.message.edit_text(HELP_OVERVIEW, reply_markup=back_to_menu_keyboard())
    await callback.answer()


@router.callback_query(F.data == "menu:chat_id")
async def handle_menu_chat_id(callback: CallbackQuery) -> None:
    if callback.message is not None:
        await callback.message.edit_text(CHAT_ID_MENU, reply_markup=back_to_menu_keyboard())
    await callback.answer()


@router.callback_query(F.data == "menu:contact")
async def handle_menu_contact(callback: CallbackQuery) -> None:
    if callback.message is not None:
        await callback.message.edit_text(CONTACT_HELP, reply_markup=back_to_menu_keyboard())
    await callback.answer()


@router.callback_query(F.data == "menu:raw")
async def handle_menu_raw(callback: CallbackQuery) -> None:
    if callback.message is not None:
        await callback.message.edit_text(RAW_MENU, reply_markup=back_to_menu_keyboard())
    await callback.answer()


@router.callback_query(F.data == "menu:diagnostics")
async def handle_menu_diagnostics(callback: CallbackQuery) -> None:
    if callback.message is not None:
        await callback.message.edit_text(DIAGNOSTICS_MENU, reply_markup=back_to_menu_keyboard())
    await callback.answer()


@router.message(Command("id"))
async def handle_id(message: Message) -> None:
    log_message_event(message, "command", command="id")
    await message.answer(format_chat(message.chat, message))


@router.message(Command("support_card"))
async def handle_support_card(message: Message) -> None:
    log_message_event(message, "command", command="support_card")
    if message.from_user is None:
        await message.answer("Telegram did not include user data in this update.")
        return
    await message.answer(format_support_card(message.from_user))


@router.message(Command("contact"))
async def handle_contact_help(message: Message) -> None:
    log_message_event(message, "command", command="contact")
    await message.answer(CONTACT_HELP)


@router.message(F.forward_origin | F.forward_from | F.forward_from_chat | F.forward_sender_name)
async def handle_forwarded_origin(message: Message, bot: Bot) -> None:
    log_message_event(message, "forwarded_origin")
    enriched_chat = await get_forwarded_chat_details(message, bot)
    await message.answer(format_contact_lookup(message, enriched_chat=enriched_chat))


async def get_forwarded_chat_details(message: Message, bot: Bot) -> Chat | None:
    chat_id: int | None = None
    if isinstance(message.forward_origin, MessageOriginChannel):
        chat_id = message.forward_origin.chat.id
    elif isinstance(message.forward_origin, MessageOriginChat):
        chat_id = message.forward_origin.sender_chat.id
    elif message.forward_from_chat:
        chat_id = message.forward_from_chat.id

    if chat_id is None:
        return None

    try:
        return await bot.get_chat(chat_id)
    except TelegramAPIError:
        return None


@router.message(Command("raw"))
async def handle_raw(message: Message) -> None:
    log_message_event(message, "command", command="raw")
    data = redact(message.model_dump(mode="json", exclude_none=True))
    text = compact_json(data)
    if len(text) > 3500:
        text = text[:3500] + "\n...[truncated]"
    await message.answer(preformatted(text))


@router.message(Command("raw_full"))
async def handle_raw_full(message: Message) -> None:
    log_message_event(message, "command", command="raw_full")
    if not message.text or "confirm" not in message.text.lower().split():
        await message.answer(RAW_FULL_WARNING)
        return
    text = compact_json(message.model_dump(mode="json", exclude_none=True))
    if len(text) > 3500:
        text = text[:3500] + "\n...[truncated]"
    await message.answer(preformatted(text))


@router.message(Command("diagnose"))
async def handle_diagnose(message: Message, bot: Bot) -> None:
    log_message_event(message, "command", command="diagnose")
    errors: list[str] = []
    chat = None
    bot_member = None
    member_count = None

    try:
        chat = await bot.get_chat(message.chat.id)
    except TelegramAPIError as exc:
        errors.append(f"getChat failed: {exc.__class__.__name__}")

    try:
        member_count = await bot.get_chat_member_count(message.chat.id)
    except TelegramAPIError as exc:
        errors.append(f"getChatMemberCount failed: {exc.__class__.__name__}")

    try:
        me = await bot.get_me()
        bot_member = await bot.get_chat_member(message.chat.id, me.id)
    except TelegramAPIError as exc:
        errors.append(f"getChatMember(bot) failed: {exc.__class__.__name__}")

    await message.answer(
        format_diagnostics(
            message,
            chat=chat,
            bot_member=bot_member,
            member_count=member_count,
            errors=errors,
        )
    )


@router.message(Command("help"))
async def handle_help(message: Message) -> None:
    log_message_event(message, "command", command="help")
    await message.answer(HELP_OVERVIEW, reply_markup=start_keyboard())


@router.message(Command(*HELP_TEXTS.keys()))
async def handle_help_topic(message: Message) -> None:
    log_message_event(message, "command", command="help_topic")
    command = message.text.split(maxsplit=1)[0].lstrip("/") if message.text else ""
    await message.answer(HELP_TEXTS.get(command, HELP_TEXTS["help_user_id"]))


@router.message(F.text.regexp(r"^@[A-Za-z0-9_]{5,32}$"))
async def handle_username_lookup(message: Message, bot: Bot) -> None:
    log_message_event(message, "username_lookup")
    username = message.text.strip()
    try:
        chat = await bot.get_chat(username)
    except TelegramAPIError as exc:
        await message.answer(
            "Telegram did not return data for this username.\n"
            f"Reason: <code>{exc.__class__.__name__}</code>\n"
            "The chat may be private, inaccessible, deleted or not exposed to bots."
        )
        return
    member_count = None
    try:
        member_count = await bot.get_chat_member_count(chat.id)
    except TelegramAPIError:
        member_count = None
    await message.answer(format_chat_lookup(chat, member_count=member_count))


@router.message()
async def handle_default(message: Message) -> None:
    if message.chat.type == "private":
        await handle_start(message)
        return
    await handle_id(message)
