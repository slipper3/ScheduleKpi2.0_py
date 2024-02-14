# --- This file is responsible for getting data from database ---

import psycopg2
from bot.data.escape import kapcha
from datetime import datetime

# --- Load database config ---
import os
from dotenv import load_dotenv

from bot.utils.log_conf import setup_logging

load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

logger = setup_logging()
 
# --- Get data from database ---
async def get_schedule_data(chatid: int, weektype: str, day: str, time: str):
    """Gets value of `chatid` - id of chat that linked with group\n
    Return linked group\`s schedule as JSON object"""

    conn = None

    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        with conn.cursor() as cursor:
            cursor.execute("""SELECT groupid FROM public.telegram
                           JOIN public.groups ON telegram.groupname = groups.groupname 
                           WHERE (telegram.chatid) = (%s)""", (chatid,))
            result = cursor.fetchone()
            cursor.execute("""SELECT lessonname, teachername, link 
                           FROM public.groups 
                           JOIN public.schedule ON groups.groupid = schedule.groupid 
                           WHERE (schedule.groupid) = (%s) AND schedule.weektype = (%s) AND schedule.dayofweek = (%s) AND schedule.lessontime = (%s)""",(result[0], weektype, day, time))
            result = cursor.fetchall()
        return result
    except Exception as er:
        logger.error(f"Error coused in get_schedule_data: {er}")
        return None
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

async def get_chats():
    """Return chats\`s id as array"""

    conn = None

    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        with conn.cursor() as cursor:
            cursor.execute("""SELECT chatid FROM public.telegram""")
            result = cursor.fetchall()
        return result
    except Exception as er:
        logger.error(f"Error coused in get_chats: {er}")
        return None
    finally:
        if conn is not None:
            conn.commit()
            conn.close()