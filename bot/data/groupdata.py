# --- File is responsible for saving university group for each telegram group ---
import psycopg2
from bot.data.escape import pg_escape_string
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

# --- Save group data ---
async def db_save_group(chatid, groupname):
    """Gets value of `chatid` - id of chat that will be linked with group
    and `groupname` - name of that group, the same as specified on the site\n
    If groupname already exist return false
    else save chatid and groupname to database"""

    conn = None
    escaped = pg_escape_string(groupname)
    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        with conn.cursor() as cursor:
            cursor.execute("""SELECT groupname FROM public.telegram WHERE groupname = (%s)""", (escaped,))
            resoult = cursor.fetchone()
            if resoult == None:
                cursor.execute("""INSERT INTO public.telegram(chatid, groupname) VALUES (%s, %s)""", (chatid, escaped))
            else: return False
        return True
    except Exception as er:
        logger.error(f"Error coused in db_save_group: {er}")
        return False
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

# --- Save pass ---
async def db_set_password(chatid, pasword: str):
    """"""

    conn = None
    escaped = pg_escape_string(pasword)
    try:
        conn = psycopg2.connect(
            host=host,
            dbname=dbname,
            user=user,
            password=password,
            port=port
        )
        with conn.cursor() as cursor:
            cursor.execute("""INSERT INTO public.telegram(password) VALUES (%s) WHERE chatid = (%s)""", (escaped, chatid))
        return True
    except Exception as er:
        return False
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

# --- Get Pass ---
async def db_get_password(chatid):
    """"""

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
            cursor.execute("""SELECT password FROM public.telegram WHERE chatid = (%s)""", (chatid,))
            result = cursor.fetchone()
            return result[0]
    except Exception as er:
        return False
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

# --- Remove group data ---
async def db_remove_group(chatid) -> None:
    """Gets value of `chatid` - id of chat that was linked with group\n
    Delete row in database that contain `chatid`"""

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
            cursor.execute("""DELETE FROM public.telegram WHERE chatid = (%s)""", (chatid,))
        return True
    except Exception as er:
        logger.error(f"Error coused in db_remove_group: {er}")
        return False
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

# --- Get group data ---
async def db_get_group(chatid):
    """Gets value of `chatid` - id of chat that is linked with group\n
    Show `groupname` in row contain `chatid`"""

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
            cursor.execute("""SELECT groupname FROM public.telegram WHERE chatid = (%s)""", (chatid,))
            result = cursor.fetchone()
        return result[0]
    except Exception as er:
        logger.error(f"Error coused in db_get_group: {er}")
        return None
    finally:
        if conn is not None:
            conn.commit()
            conn.close()

async def db_condig_emoji(chatid) -> str:

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
            cursor.execute("""SELECT emoji FROM public.telegram WHERE chatid = (%s)""", (chatid,))
            result = cursor.fetchone()
            state = not result[0]
            cursor.execute("""UPDATE public.telegram SET emoji = (%s::boolean) WHERE chatid = (%s)""", (state, chatid))
        return str(state)
    except Exception as er:
        logger.error(f"Error coused in db_condig_emoji: {er}")
        return None
    finally:
        if conn is not None:
            conn.commit()
            conn.close()