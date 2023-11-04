import asyncio
from aiogram import Bot, Dispatcher
from handlers import commands
from misc.env import TgKeys


async def main():
    bot = Bot(token=TgKeys.TOKEN, parse_mode='HTML')
    dp = Dispatcher()

    dp.include_routers(
        commands.router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())