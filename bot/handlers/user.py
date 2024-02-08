from aiogram import Bot, types, Router
from aiogram.filters import Command

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot.data.groupdata import *

user_router = Router()

@user_router.message(Command("start"))
async def start(message: types.Message) -> None:
    await message.answer("Hi")


@user_router.message(Command("info"))
async def info(message: types.Message) -> None:
    pass


class states(StatesGroup):
    group = State()
@user_router.message(Command("set"))
async def set_group(message: types.Message, state: FSMContext) -> None:
    await state.set_state(states.group)
    await message.answer("Вкажіть групу")
@user_router.message(states.group)
async def save_group(message: types.Message, state: FSMContext) -> None:
    if await db_save_group(message.chat.id, message.text):
        await message.answer("Група успішно збережена")
    else: await message.answer("Невірний запит, спробуйте ще раз")
    await state.clear()


@user_router.message(Command("remove"))
async def remove_group(message: types.Message) -> None:
    if await db_remove_group(message.chat.id):
        await message.answer("Група успішно видалена")
    else: await message.answer("Помилка видалення групи")


@user_router.message(Command("get"))
async def get_group(message: types.Message) -> None:
    groupName = await db_get_group(message.chat.id)
    if groupName != None:
        await message.answer(f"Ваша група: {groupName}")
    else: await message.answer("До вашого чату група не прикріплена")