from __future__ import annotations

from html import escape
from typing import Any

from aiogram.types import (
    Chat,
    Message,
    MessageOriginChannel,
    MessageOriginChat,
    MessageOriginHiddenUser,
    MessageOriginUser,
    User,
)

REPOSITORY_URL = "https://github.com/se1dhe/getid-bot"
USER_EXTRA_FIELDS = (
    "is_premium",
    "language_code",
    "added_to_attachment_menu",
    "can_join_groups",
    "can_read_all_group_messages",
    "supports_inline_queries",
)
CHAT_EXTRA_FIELDS = (
    "is_forum",
    "active_usernames",
    "description",
    "bio",
    "linked_chat_id",
    "accent_color_id",
    "profile_accent_color_id",
)


def code(value: object) -> str:
    return f"<code>{escape(str(value))}</code>"


def value_or_dash(value: object | None) -> str:
    return "-" if value is None else str(value)


def format_user(user: User) -> str:
    username = f"@{user.username}" if user.username else "-"
    full_name = user.full_name or "-"
    lines = [
        "<b>Telegram diagnostics</b>",
        "I can show IDs, chat metadata, forum topic IDs and sanitized raw updates.",
        "",
        "<b>Your identity</b>",
        f"User ID: {code(user.id)}",
        f"Username: {code(username)}",
        f"Name: {escape(full_name)}",
        f"Language: {code(value_or_dash(user.language_code))}",
        f"Is bot: {code(user.is_bot)}",
    ]
    if user.is_premium is not None:
        lines.append(f"Premium: {code(user.is_premium)}")
    lines.extend(
        [
            "",
            "<b>Try next</b>",
            "/id - show current chat, message and topic IDs",
            "/contact - how to inspect a forwarded user, chat or channel",
            "/raw - show sanitized raw Telegram update JSON",
            "/diagnose - explain bot permissions and privacy limits",
            "/support_card - create a minimal card for support",
            "Forward any message here to inspect its user, chat or channel origin.",
            "Send @channel_username here to look up a public channel or group.",
            "",
            "<b>Open source</b>",
            f"Source code: {REPOSITORY_URL}",
            "This bot uses only official Telegram Bot API data.",
        ]
    )
    return "\n".join(lines)


def format_chat(chat: Chat, message: Message) -> str:
    lines = [
        "<b>Telegram chat diagnostics</b>",
        f"Chat ID: {code(chat.id)}",
        f"Chat type: {code(chat.type)}",
        f"Title: {escape(value_or_dash(chat.title))}",
        f"Username: {code('@' + chat.username if chat.username else '-')}",
        f"Message ID: {code(message.message_id)}",
    ]
    if message.message_thread_id is not None:
        lines.append(f"Topic ID: {code(message.message_thread_id)}")
    lines.append("")
    lines.append(
        "If some messages are invisible, check BotFather privacy mode and bot admin rights."
    )
    return "\n".join(lines)


def format_support_card(user: User) -> str:
    username = f"@{user.username}" if user.username else "-"
    return "\n".join(
        [
            "<b>Support identity card</b>",
            f"Telegram ID: {code(user.id)}",
            f"Username: {code(username)}",
            f"Name: {escape(user.full_name or '-')}",
        ]
    )


def format_chat_lookup(chat: Chat) -> str:
    lines = [
        "<b>Public chat lookup</b>",
        f"Chat ID: {code(chat.id)}",
        f"Type: {code(chat.type)}",
        f"Title: {escape(value_or_dash(chat.title))}",
        f"Username: {code('@' + chat.username if chat.username else '-')}",
    ]
    if getattr(chat, "is_forum", None) is not None:
        lines.append(f"Forum: {code(chat.is_forum)}")
    return "\n".join(lines)


def format_contact_lookup(message: Message, enriched_chat: Chat | None = None) -> str:
    origin = message.forward_origin
    if isinstance(origin, MessageOriginUser):
        return "\n".join(
            [
                "<b>Forwarded user</b>",
                format_user_details(origin.sender_user),
                "",
                "Telegram exposed this user because the forwarded message includes "
                "a public user origin.",
            ]
        )

    if isinstance(origin, MessageOriginHiddenUser):
        return "\n".join(
            [
                "<b>Forwarded hidden user</b>",
                f"Name: {escape(origin.sender_user_name)}",
                "",
                "Telegram hides this sender's user ID and username. Bots cannot bypass that.",
            ]
        )

    if isinstance(origin, MessageOriginChat):
        chat = enriched_chat or origin.sender_chat
        lines = [
            "<b>Forwarded chat</b>",
            format_chat_details(chat),
        ]
        if origin.author_signature:
            lines.append(f"Author signature: {code(origin.author_signature)}")
        lines.extend(
            [
                "",
                "Telegram exposed the chat that sent this message.",
            ]
        )
        return "\n".join(lines)

    if isinstance(origin, MessageOriginChannel):
        chat = enriched_chat or origin.chat
        lines = [
            "<b>Forwarded channel</b>",
            format_chat_details(chat),
            f"Original message ID: {code(origin.message_id)}",
        ]
        if origin.author_signature:
            lines.append(f"Author signature: {code(origin.author_signature)}")
        lines.extend(
            [
                "",
                "Telegram exposed the channel origin and original channel message ID.",
            ]
        )
        return "\n".join(lines)

    if message.forward_from:
        return "\n".join(
            [
                "<b>Forwarded user</b>",
                format_user_details(message.forward_from),
                "",
                "Telegram exposed this user through legacy forward fields.",
            ]
        )

    if message.forward_from_chat:
        chat = enriched_chat or message.forward_from_chat
        lines = [
            "<b>Forwarded chat or channel</b>",
            format_chat_details(chat),
        ]
        if message.forward_from_message_id is not None:
            lines.append(f"Original message ID: {code(message.forward_from_message_id)}")
        if message.forward_signature:
            lines.append(f"Author signature: {code(message.forward_signature)}")
        return "\n".join(lines)

    if message.forward_sender_name:
        return "\n".join(
            [
                "<b>Forwarded hidden user</b>",
                f"Name: {escape(message.forward_sender_name)}",
                "",
                "Telegram hides this sender's user ID and username. Bots cannot bypass that.",
            ]
        )

    return "\n".join(
        [
            "<b>No forwarded origin found</b>",
            "Forward a message from a user, group or channel to inspect what Telegram exposes.",
        ]
    )


def format_user_details(user: User) -> str:
    username = f"@{user.username}" if user.username else "-"
    lines = [
        f"User ID: {code(user.id)}",
        f"Username: {code(username)}",
        f"Name: {escape(user.full_name or '-')}",
        f"Is bot: {code(user.is_bot)}",
    ]
    lines.extend(format_extra_fields(user, USER_EXTRA_FIELDS))
    return "\n".join(lines)


def format_chat_details(chat: Chat) -> str:
    lines = [
        f"Chat ID: {code(chat.id)}",
        f"Type: {code(chat.type)}",
        f"Title: {escape(value_or_dash(chat.title))}",
        f"Username: {code('@' + chat.username if chat.username else '-')}",
    ]
    lines.extend(format_extra_fields(chat, CHAT_EXTRA_FIELDS))
    return "\n".join(lines)


def format_extra_fields(model: object, field_names: tuple[str, ...]) -> list[str]:
    lines: list[str] = []
    for field_name in field_names:
        value = getattr(model, field_name, None)
        if value is None:
            continue
        label = field_name.replace("_", " ").title()
        if isinstance(value, list):
            value = ", ".join(str(item) for item in value) or "-"
        lines.append(f"{label}: {code(value)}")
    return lines


def compact_json(data: dict[str, Any]) -> str:
    import json

    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
