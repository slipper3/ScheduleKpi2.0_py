# --- This file contains all admins commansds ---
from aiogram import Bot, types, Dispatcher
import os
from dotenv import load_dotenv, dotenv_values
from bot_intance import bot

load_dotenv()
dp = Dispatcher

async def shutbot(message: types.Message):
    if(str(message.from_user.id) == os.getenv("ADMIN_ID")):
        #Somehow shutdown bot
        #await dp.stop_polling(bot)
        pass