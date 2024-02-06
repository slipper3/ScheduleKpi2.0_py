# --- This file is responsible for getting data from database ---
import requests as rq
import json

import asyncio

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
async def get_data():
    pass
