# --- File is responsible for saving university group for each telegram group ---

# --- Load database config ---
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("HOST")
dbname = os.getenv("DB_NAME")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
port = os.getenv("PORT")

# --- Save group data ---
async def save_group() -> None:
    pass 

# --- Remove group data ---
async def remove_group() -> None:
    pass