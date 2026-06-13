from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .formatters import REPOSITORY_URL


def main_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="My Telegram ID", callback_data="menu:my_id"),
                InlineKeyboardButton(text="Chat ID", callback_data="menu:chat_id"),
            ],
            [
                InlineKeyboardButton(text="Forwarded contact", callback_data="menu:contact"),
                InlineKeyboardButton(text="Raw update JSON", callback_data="menu:raw"),
            ],
            [
                InlineKeyboardButton(text="Diagnostics", callback_data="menu:diagnostics"),
                InlineKeyboardButton(text="Help", callback_data="menu:help"),
            ],
            [InlineKeyboardButton(text="GitHub", url=REPOSITORY_URL)],
        ]
    )


def back_to_menu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Back to menu", callback_data="menu:home")],
            [InlineKeyboardButton(text="GitHub", url=REPOSITORY_URL)],
        ]
    )


def start_keyboard() -> InlineKeyboardMarkup:
    return main_menu_keyboard()
