from aiogram import Bot, Dispatcher
import asyncio
import logging

from config import settings
from routers import router

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
dp.include_router(router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
