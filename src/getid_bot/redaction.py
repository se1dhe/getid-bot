from __future__ import annotations

import re
from collections.abc import Mapping, Sequence
from typing import Any

SENSITIVE_KEYS = {
    "token",
    "phone_number",
    "email",
    "invite_link",
    "url",
    "text",
    "caption",
    "web_app_data",
    "data",
    "credential",
    "secret",
    "password",
    "file_id",
    "file_unique_id",
    "passport_data",
    "successful_payment",
    "invoice_payload",
    "shipping_address",
    "order_info",
}

EMAIL_RE = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
PHONE_RE = re.compile(r"(?<!\d)\+?\d[\d\s().-]{7,}\d(?!\d)")
BOT_TOKEN_RE = re.compile(r"\b\d{5,}:[A-Za-z0-9_-]{20,}\b")
INVITE_RE = re.compile(r"https?://t\.me/(?:joinchat/|\+)[A-Za-z0-9_-]+", re.IGNORECASE)


def redact_text(value: str) -> str:
    value = BOT_TOKEN_RE.sub("[REDACTED_TOKEN]", value)
    value = INVITE_RE.sub("[REDACTED_INVITE_LINK]", value)
    value = EMAIL_RE.sub("[REDACTED_EMAIL]", value)
    value = PHONE_RE.sub("[REDACTED_PHONE]", value)
    return value


def redact(value: Any) -> Any:
    if isinstance(value, Mapping):
        redacted: dict[str, Any] = {}
        for key, item in value.items():
            key_text = str(key)
            if key_text.lower() in SENSITIVE_KEYS:
                redacted[key_text] = redact_key_value(key_text)
            else:
                redacted[key_text] = redact(item)
        return redacted

    if isinstance(value, str):
        return redact_text(value)

    if isinstance(value, Sequence) and not isinstance(value, bytes | bytearray):
        return [redact(item) for item in value]

    return value


def redact_key_value(key: str) -> str:
    if key.lower() in {"text", "caption", "data"}:
        return "[REDACTED_TEXT]"
    return "[REDACTED]"
