from aiogram import Bot, types, Router
from aiogram.filters import Command

user_router = Router()

@user_router.message(Command("start"))
async def start() -> None:
    pass

@user_router.message(Command("info"))
async def info() -> None:
    pass

@user_router.message(Command("set"))
async def set_group() -> None:
    pass

@user_router.message(Command("remove"))
async def remove_group() -> None:
    pass

@user_router.message(Command("get"))
async def get_group() -> None:
    pass