from aiogram.types import Chat, Message, User

from getid_bot.formatters import format_chat, format_support_card, format_user


def test_format_user_preserves_large_id() -> None:
    user = User(id=9007199254740993, is_bot=False, first_name="Ada", username="ada")

    text = format_user(user)

    assert "9007199254740993" in text
    assert "@ada" in text
    assert "/raw" in text
    assert "/diagnose" in text
    assert "https://github.com/se1dhe/getid-bot" in text


def test_format_chat_includes_topic_id() -> None:
    chat = Chat(id=-1001234567890, type="supergroup", title="Builders")
    message = Message(message_id=42, date=0, chat=chat, message_thread_id=777)

    text = format_chat(chat, message)

    assert "-1001234567890" in text
    assert "42" in text
    assert "777" in text


def test_support_card_is_minimal() -> None:
    user = User(id=123, is_bot=False, first_name="Ada", last_name="Lovelace")

    text = format_support_card(user)

    assert "Telegram ID" in text
    assert "123" in text
    assert "Language" not in text
