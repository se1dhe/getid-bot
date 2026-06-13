import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from .config import load_settings
from .handlers import router


async def run_polling() -> None:
    settings = load_settings()
    logging.basicConfig(
        level=settings.log_level.upper(),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    parse_mode = ParseMode.HTML if settings.bot_parse_mode.upper() == "HTML" else None
    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=parse_mode),
    )
    dispatcher = Dispatcher()
    dispatcher.include_router(router)

    await dispatcher.start_polling(bot, allowed_updates=dispatcher.resolve_used_update_types())


def run() -> None:
    asyncio.run(run_polling())

