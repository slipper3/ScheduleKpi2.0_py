# --- This file contains all admins commansds ---
import sys
from bot.data.scheduledata import get_chats, get_schedule_data
from bot.utils.apschedule import schedul
from bot.utils.log_conf import setup_logging
from bot_intance import bot
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command

import os
from dotenv import load_dotenv

load_dotenv()

admin_router = Router()

logger = setup_logging()

@admin_router.startup()
async def startup(bot: Bot) -> None:
    await bot.send_message(chat_id=int(os.getenv("ADMIN_ID")), text="Bot is online")
    logger.info("Bot is online")

@admin_router.shutdown()
async def shoutdown(bot: Bot) -> None:
    await bot.send_message(chat_id=int(os.getenv("ADMIN_ID")), text="Bot is ofline")
    logger.info("Bot is ofline")

def shutdown_handler(dp: Dispatcher):
    @admin_router.message(Command("shutdown"))
    async def shutbot(message: types.Message):
        if message.from_user.id == int(os.getenv("ADMIN_ID")):
            # Send a message indicating the bot is shutting down
            logger.info("Bot is shutting down...")       
            # Close the bot
            await dp.storage.close()
            #await dp.storage.wait_closed()
            await bot.close()        
            # Gracefully stop the program
            await sys.exit()

#Any test i need i can add here

@admin_router.message(Command("sched_test"))
async def test_(message: types.Message):
     if message.from_user.id == int(os.getenv("ADMIN_ID")):
        test = await schedul(time="10:25", bot=bot)
        await message.answer(f"Schedul data for: curent day, current week\n{test}")