from getid_bot.keyboards import back_to_menu_keyboard, main_menu_keyboard


def button_texts(keyboard) -> list[str]:
    return [button.text for row in keyboard.inline_keyboard for button in row]


def callback_data(keyboard) -> list[str | None]:
    return [button.callback_data for row in keyboard.inline_keyboard for button in row]


def test_main_menu_keyboard_has_clear_sections() -> None:
    keyboard = main_menu_keyboard()

    assert button_texts(keyboard) == [
        "My Telegram ID",
        "Chat ID",
        "Forwarded contact",
        "Raw update JSON",
        "Diagnostics",
        "Help",
        "GitHub",
    ]
    assert "menu:home" not in callback_data(keyboard)


def test_back_to_menu_keyboard_returns_home() -> None:
    keyboard = back_to_menu_keyboard()

    assert "Back to menu" in button_texts(keyboard)
    assert "menu:home" in callback_data(keyboard)

