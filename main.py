from aiogram import Bot, Dispatcher
import os
import asyncio
from handlers import *

bot = Bot(os.getenv("TOKEN"))
dp = Dispatcher()

dp.include_router(handlers_router)


def on_start():
    print("Bot запущен")


async def start_bot():
    dp.startup.register(on_start)
    # Пока бот выключен все запросы удаляются
    await bot.delete_webhook(drop_pending_updates=True)
    # бот сам проверяет запросы
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())
