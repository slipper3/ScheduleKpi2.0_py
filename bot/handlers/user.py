from aiogram import Bot, types, Router
from aiogram.filters import Command
from bot_intance import bot

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from bot.data.groupdata import *
from bot.utils.texts import *
from bot.keyboards.keyboards import *
from bot.utils.log_conf import setup_logging

import os
from dotenv import load_dotenv

load_dotenv()

user_router = Router()

logger = setup_logging()

@user_router.message(Command("start"))
async def start(message: types.Message) -> None:
    await message.answer(await start_text(), reply_markup=await start_keyboard(), parse_mode='HTML')


@user_router.message(Command("info"))
async def info(message: types.Message) -> None:
    await message.answer(await info_text(), reply_markup=await info_keyboard(), parse_mode='HTML')


@user_router.message(Command("menu"))
async def menu(message: types.Message) -> None:
    await message.answer(await menu_text(), reply_markup=await menu_keyboard(), parse_mode='HTML')


class gstates(StatesGroup):
    group = State()
@user_router.message(Command("set"))
async def set_group(message: types.Message, state: FSMContext) -> None:
    await state.set_state(gstates.group)
    await message.answer("Вкажіть групу")
@user_router.message(gstates.group)
async def save_group(message: types.Message, state: FSMContext) -> None:
    if await db_save_group(message.chat.id, message.text):
        await message.answer("Група успішно збережена")
    else: 
        await message.answer("Невірний запит, спробуйте ще раз")
        logger.warning(f"User: {message.from_user.id}, tryed link {message.text} group! Group was not linked!")
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


@user_router.message(Command("emoji"))
async def config_emoji(message: types.Message) -> None:
    status = await db_condig_emoji(message.chat.id)
    await message.answer(f"Статус емоджі в вашому чаті змінено на: {status}")


@user_router.message(Command("wed"))
async def web(message: types.Message) -> None:
    await message.answer("Тут буде лінк на сайт")

class rstates(StatesGroup):
    rep = State()
@user_router.message(Command("report"))
async def get_report(message: types.Message, state: FSMContext) -> None:
    await state.set_state(rstates.rep)
    await message.answer("Напишіть своє повідомленя 📝")
@user_router.message(rstates.rep)
async def send_report(message: types.Message, state: FSMContext) -> None:
    await bot.send_message(chat_id=int(os.getenv("ADMIN_ID")), text=f"#report\n\nUserid=<code>{message.from_user.id}</code>\nUsername={message.from_user.first_name} {message.from_user.last_name}\nUsername=<code>{message.from_user.username}</code>\nChatid=<code>{message.chat.id}</code>\n\n{message.text}", parse_mode="HTML")
    await message.answer("Ваше повідомлення було надіслано розробнику.")
    await state.clear()
