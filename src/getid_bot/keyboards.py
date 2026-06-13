from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from .formatters import REPOSITORY_URL


def start_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="My ID", callback_data="menu:my_id"),
                InlineKeyboardButton(text="Help", callback_data="menu:help"),
            ],
            [
                InlineKeyboardButton(text="Contact lookup", callback_data="menu:contact"),
                InlineKeyboardButton(text="Raw JSON", callback_data="menu:raw"),
            ],
            [InlineKeyboardButton(text="GitHub", url=REPOSITORY_URL)],
        ]
    )

