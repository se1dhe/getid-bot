from __future__ import annotations

from html import escape
from typing import Any

from aiogram.types import Chat, Message, User


def code(value: object) -> str:
    return f"<code>{escape(str(value))}</code>"


def value_or_dash(value: object | None) -> str:
    return "-" if value is None else str(value)


def format_user(user: User) -> str:
    username = f"@{user.username}" if user.username else "-"
    full_name = user.full_name or "-"
    lines = [
        "<b>Your Telegram identity</b>",
        f"User ID: {code(user.id)}",
        f"Username: {code(username)}",
        f"Name: {escape(full_name)}",
        f"Language: {code(value_or_dash(user.language_code))}",
        f"Is bot: {code(user.is_bot)}",
    ]
    if user.is_premium is not None:
        lines.append(f"Premium: {code(user.is_premium)}")
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


def compact_json(data: dict[str, Any]) -> str:
    import json

    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
