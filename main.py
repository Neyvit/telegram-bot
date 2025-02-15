import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import BotCommandScopeAllPrivateChats

from dotenv import find_dotenv, load_dotenv

from common.bot_commands_list import private
from handlers import commands, portfolio, faq

load_dotenv(find_dotenv())

async def main():
    bot = Bot(token=os.getenv('TTOKKEN_APE'))
    dp = Dispatcher()

    # Регистрируем все роутеры
    dp.include_router(commands.router)
    dp.include_router(portfolio.router)
    dp.include_router(faq.router)

    # Устанавливаем команды бота
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=private, scope=BotCommandScopeAllPrivateChats())
    
    # Запускаем бота
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
