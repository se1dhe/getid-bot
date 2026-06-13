from __future__ import annotations

from aiogram import Bot, F, Router
from aiogram.exceptions import TelegramAPIError
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from .formatters import (
    compact_json,
    format_chat,
    format_chat_lookup,
    format_support_card,
    format_user,
)
from .help_texts import HELP_TEXTS
from .redaction import redact

router = Router()


@router.message(CommandStart())
async def handle_start(message: Message) -> None:
    if message.from_user is None:
        await message.answer("Telegram did not include user data in this update.")
        return
    await message.answer(format_user(message.from_user))


@router.message(Command("id"))
async def handle_id(message: Message) -> None:
    await message.answer(format_chat(message.chat, message))


@router.message(Command("support_card"))
async def handle_support_card(message: Message) -> None:
    if message.from_user is None:
        await message.answer("Telegram did not include user data in this update.")
        return
    await message.answer(format_support_card(message.from_user))


@router.message(Command("raw"))
async def handle_raw(message: Message) -> None:
    data = redact(message.model_dump(mode="json", exclude_none=True))
    text = compact_json(data)
    if len(text) > 3500:
        text = text[:3500] + "\n...[truncated]"
    await message.answer(f"<pre>{text}</pre>")


@router.message(Command("diagnose"))
async def handle_diagnose(message: Message, bot: Bot) -> None:
    lines = [
        "<b>Diagnostics</b>",
        f"Chat type: <code>{message.chat.type}</code>",
        f"Chat ID: <code>{message.chat.id}</code>",
    ]
    if message.message_thread_id is not None:
        lines.append(f"Topic ID: <code>{message.message_thread_id}</code>")

    try:
        me = await bot.get_me()
        member = await bot.get_chat_member(message.chat.id, me.id)
        lines.append(f"Bot status: <code>{member.status}</code>")
    except TelegramAPIError as exc:
        lines.append(f"Bot status check failed: <code>{exc.__class__.__name__}</code>")

    lines.extend(
        [
            "",
            "If regular group messages are missing, check BotFather privacy mode.",
            "Telegram does not expose private users, hidden members or inaccessible chats to bots.",
        ]
    )
    await message.answer("\n".join(lines))


@router.message(Command(*HELP_TEXTS.keys()))
async def handle_help_topic(message: Message) -> None:
    command = message.text.split(maxsplit=1)[0].lstrip("/") if message.text else ""
    await message.answer(HELP_TEXTS.get(command, HELP_TEXTS["help_user_id"]))


@router.message(F.text.regexp(r"^@[A-Za-z0-9_]{5,32}$"))
async def handle_username_lookup(message: Message, bot: Bot) -> None:
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
    await message.answer(format_chat_lookup(chat))


@router.message()
async def handle_default(message: Message) -> None:
    if message.chat.type == "private":
        await handle_start(message)
        return
    await handle_id(message)
