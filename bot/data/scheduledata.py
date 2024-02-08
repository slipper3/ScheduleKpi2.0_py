# --- This file is responsible for getting data from database ---

import psycopg2
from bot.data.kapcha import kapcha

# --- Load database config ---
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")


# --- Get data from database ---
async def get_schedule_data(chatid, weektype):
    """Gets value of `chatid` - id of chat that linked with group\n
    Return linked group\`s schedule as JSON object"""

    # Check sql request
    if await kapcha(chatid, "chatID") == False:
        return False
    
    # get weektype
    #weektype = "firstWeek"

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
            cursor.execute("""SELECT dayofweek, lessontime, lessonname, teachername, link 
                           FROM public.groups 
                           JOIN public.schedule ON groups.groupid = schedule.groupid 
                           WHERE (schedule.groupid) = (%s) AND schedule.weektype = (%s)""",(result[0], weektype))
            result = cursor.fetchall()
        return result
    except Exception as er:
        print("Request error", er)
        return None
    finally:
        conn.commit()
        conn.close()
