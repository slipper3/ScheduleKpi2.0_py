# --- This file is responsible for sending scheduled messages ---
from bot.data.scheduledata import *
from datetime import datetime
import pytz

from aiogram import Bot, types

import random
from bot.utils.stikers import stickers
from bot.utils.log_conf import setup_logging

import os
from dotenv import load_dotenv

template = {
    0: "Пн",
    1: "Вт",
    2: "Ср",
    3: "Чт",
    4: "Пт",
    5: "Сб",
    6: "Нд"
}

logger = setup_logging()

load_dotenv()

async def schedul(time: str, bot: Bot, admin: bool = False):
    """Send message to all registered in database chats\n
    Take lesson for each grgoup in given time
    Also sent stickers if thay dont disable"""

    # get current time
    timezone = pytz.timezone('Europe/Kiev')
    current = datetime.now(timezone)
    # get current day (mon - 0, sun - 6)
    day = current.weekday()
    # get number of current week
    week = current.isocalendar()[1] 

    weektype = ""
    if week % 2 == 0:
        weektype = "secondWeek"
    else: weektype = "firstWeek"

    logger.info(f"Schedule acted with data: weektype-{weektype}, day-{template[day]}, time-{time}")
    chats = await get_chats()
    for chat in chats:
        if chat[0] == None:
            logger.warning(f"Chat id id None")
            continue
        sched = await get_schedule_data(chatid=chat[0], weektype=weektype, day=template[day], time=time)
        if sched == None: # If schedule wasnt filled
            logger.warning(f"No schedule for chat {chat[0]}")
            continue
        for pair in sched:
            if pair[2] != "" and pair[1] != "" and pair[0] != "":
                text = [
                            f"💃 <b>О {time} вас чекає пара</b> 🕺\n",
                            f"🔸{pair[0]})",
                            f"🔸Разом з {pair[1]}\n",
                            f"<a href='{pair[2]}'>Посилання на пару</a>\n"
                        ]
                await bot.send_message(chat_id=chat[0], text='\n'.join(text), parse_mode='HTML')
                await bot.send_sticker(chat_id=chat[0], sticker=stickers[random.randint(0,len(stickers)-1)])
            elif pair[1] != "" and pair[0] != "":
                text = [
                            f"💃 <b>О {time} вас чекає пара</b> 🕺\n",
                            f"🔸{pair[0]})",
                            f"🔸Разом з {pair[1]}\n",
                        ]
                await bot.send_message(chat_id=chat[0], text='\n'.join(text), parse_mode='HTML')
                await bot.send_sticker(chat_id=chat[0], sticker=stickers[random.randint(0,len(stickers)-1)])
            elif pair[0] != "":
                text = [
                            f"💃 <b>О {time} вас чекає пара</b> 🕺\n",
                            f"🔸{pair[0]})",
                        ]
                await bot.send_message(chat_id=chat[0], text='\n'.join(text), parse_mode='HTML')
                await bot.send_sticker(chat_id=chat[0], sticker=stickers[random.randint(0,len(stickers)-1)])
            else:
                text = [
                            f"💃 <b>О {time} вас чекає пара</b> 🕺\n",
                            f"🔸{pair[0]})",
                        ]
                await bot.send_message(chat_id=chat[0], text='\n'.join(text), parse_mode='HTML')
                await bot.send_sticker(chat_id=chat[0], sticker=stickers[random.randint(0,len(stickers)-1)])