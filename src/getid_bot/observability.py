from __future__ import annotations

import json
import logging
from typing import Any

from aiogram.types import Message

logger = logging.getLogger("getid_bot")


def log_message_event(message: Message, event: str, **fields: Any) -> None:
    payload = {
        "event": event,
        "chat_type": message.chat.type,
        "chat_id": str(message.chat.id),
        "message_id": message.message_id,
    }
    if message.message_thread_id is not None:
        payload["message_thread_id"] = message.message_thread_id
    payload.update({key: str(value) for key, value in fields.items() if value is not None})
    logger.info(json.dumps(payload, sort_keys=True))

