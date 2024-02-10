# --- This file contains all admins commansds ---
from bot.data.scheduledata import get_chats, get_schedule_data
from bot.utils.apschedule import schedul
from bot_intance import bot
from aiogram import Bot, types, Router
from aiogram.filters import Command

import os
from dotenv import load_dotenv

load_dotenv()

admin_router = Router()

@admin_router.startup()
async def startup(bot: Bot) -> None:
    bot.send_message(chat_id=int(os.getenv("ADMIN_ID")), text="Bot is online")

@admin_router.shutdown()
async def shoutdown(bot: Bot) -> None:
    bot.send_message(chat_id=int(os.getenv("ADMIN_ID")), text="Bot is ofline")

# @admin_router.message(Command("shutdown"))
# async def shutbot(message: types.Message):
#     if message.from_user.id == int(os.getenv("ADMIN_ID")):
#          # Send a message indicating the bot is shutting down
#         await message.answer("Bot is shutting down...")
        
#         # Close the bot
#         await bot.close()

#         # Optionally, stop the event loop
#         # await dp.storage.close()
#         # await dp.storage.wait_closed()
        
#         # Gracefully stop the program
#         exit()


# @admin_router.message(Command("test"))
# async def test_(message: types.Message):
#     #test = await get_schedule_data(message.chat.id, "firstWeek")
#     # test = await schedul("10:25", bot)
#     # print(test)
#     # test = await schedul("12:20", bot)
#     # print(test)
#     pass