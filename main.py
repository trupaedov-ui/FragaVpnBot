import asyncio

from aiogram import Bot, Dispatcher

from config.config import BOT_TOKEN
from db.database import init_db
from handlers import buy

from handlers import start, buy, admin


async def main():
    await init_db()

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(buy.router)
    dp.include_router(admin.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())