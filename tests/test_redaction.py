from getid_bot.redaction import redact, redact_text


def test_redact_text_masks_common_sensitive_values() -> None:
    text = "token 123456:ABCdefghi_jklmnopqrstuvwxyz email a@b.com phone +380 67 123 45 67"

    redacted = redact_text(text)

    assert "123456:" not in redacted
    assert "a@b.com" not in redacted
    assert "+380" not in redacted
    assert "[REDACTED_TOKEN]" in redacted
    assert "[REDACTED_EMAIL]" in redacted
    assert "[REDACTED_PHONE]" in redacted


def test_redact_masks_sensitive_keys_recursively() -> None:
    payload = {
        "message": {
            "invite_link": "https://t.me/+secret",
            "from": {"id": 123, "email": "user@example.com"},
            "items": [{"phone_number": "+1 555 123 4567"}],
        }
    }

    redacted = redact(payload)

    assert redacted["message"]["invite_link"] == "[REDACTED]"
    assert redacted["message"]["from"]["email"] == "[REDACTED]"
    assert redacted["message"]["items"][0]["phone_number"] == "[REDACTED]"


def test_redact_masks_message_text_and_callback_data() -> None:
    payload = {
        "message": {"text": "private support request"},
        "callback_query": {"data": "user:123:secret"},
        "channel_post": {"caption": "private caption"},
    }

    redacted = redact(payload)

    assert redacted["message"]["text"] == "[REDACTED_TEXT]"
    assert redacted["callback_query"]["data"] == "[REDACTED_TEXT]"
    assert redacted["channel_post"]["caption"] == "[REDACTED_TEXT]"
