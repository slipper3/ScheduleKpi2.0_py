import os
from dotenv import load_dotenv, dotenv_values
from bot_intance import bot

from bot.handlers.basic import *

import asyncio
from aiogram import Dispatcher, types
from aiogram.filters import Command, CommandStart

load_dotenv()
dp = Dispatcher()

#@dp.message(CommandStart())
#async def echo(message: types.Message):
#    await message.answer("I am working!")

async def main() -> None:
    dp.startup.register(startup)
    dp.shutdown.register(shoutdown)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
