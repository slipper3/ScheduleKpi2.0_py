# --- This file contains all admins commansds ---
from aiogram import Bot, types, Router
from aiogram.filters import Command

import os
from dotenv import load_dotenv

load_dotenv()

admin_router = Router()

@admin_router.startup()
async def startup(bot: Bot) -> None:
    #await set_commands(bot)
    print("Bot is online")

@admin_router.shutdown()
async def shoutdown(bot: Bot) -> None:
    print("Bot is ofline")

@admin_router.message(Command("shutdown"))
async def shutbot(message: types.Message):
    if(str(message.from_user.id) == os.getenv("ADMIN_ID")):
        #Somehow shutdown bot
        #await dp.stop_polling(bot)
        pass