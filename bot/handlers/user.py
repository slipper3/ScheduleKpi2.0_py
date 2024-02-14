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

# --- Set group
class gstates(StatesGroup):
    group = State()
    pas = State()
@user_router.message(Command("set"))
async def set_group(message: types.Message, state: FSMContext) -> None:
    if await db_get_group(message.chat.id) == None:
        await state.set_state(gstates.group)
        await message.answer("Вкажіть групу")
    else: 
        await message.answer("У вашому чаті уже закриплена група")
@user_router.message(gstates.group)
async def save_group(message: types.Message, state: FSMContext) -> None:
    if await db_save_group(message.chat.id, message.text):
        await message.answer("Група успішно збережена\n\nСтворіть пароль для редагування розкладу\nНапишіть d якщо хочете залишити пароль за замовчуванням \"1111\"")
        await state.set_state(gstates.pas)
    else: 
        await message.answer("<b>Невірний запит!</b>\nВведено некоректні данні або така група вже закріплена за іншим чатом", parse_mode="HTML")
        logger.warning(f"User: {message.from_user.id}, tryed link {message.text} group! Group was not linked!")
        await state.clear()
@user_router.message(gstates.pas)
async def set_passeord(message: types.Message, state: FSMContext):
    if message.text == "d":
        message.answer("Встановлено пароль за замовчуванням")
    else:
        db_set_password(message.chat.id, message.text)
    await state.clear()

# --- Remove group
@user_router.message(Command("remove"))
async def remove_group(message: types.Message) -> None:
    if await db_remove_group(message.chat.id):
        await message.answer("Група успішно видалена")
    else: await message.answer("Помилка видалення групи")

# --- Show group
@user_router.message(Command("get"))
async def get_group(message: types.Message) -> None:
    groupName = await db_get_group(message.chat.id)
    if groupName != None:
        await message.answer(f"Ваша група: {groupName}")
    else: await message.answer("До вашого чату група не прикріплена")

# --- Change emoji status
@user_router.message(Command("emoji"))
async def config_emoji(message: types.Message) -> None:
    status = await db_condig_emoji(message.chat.id)
    await message.answer(f"Статус емоджі в вашому чаті змінено на: {status}")

# --- Show link to site
@user_router.message(Command("wed"))
async def web(message: types.Message) -> None:
    await message.answer("Тут буде лінк на сайт")

# --- Send report to developer
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

# --- Change pass
class pstates(StatesGroup):
    old_pas = State()
    pas = State()
@user_router.message(Command("ch_pass"))
async def chenge_password(message: types.Message, state: FSMContext):
    await message.answer("Введіть старий пароль: ")
    await state.set_state(pstates.old_pas)
@user_router.message(pstates.old_pas)
async def save_password(message: types.Message, state: FSMContext):
    if message.text == await db_get_password(message.chat.id):
        await message.answer("Введіть новий пароль: ")
        await state.set_state(pstates.pas)
    elif await db_get_password(message.chat.id) == False:
        await message.answer("🟡 Помилка запиту")
        await state.clear()
    else:
        await message.answer("🔴 Невірний пароль")
        await state.clear()
@user_router.message(pstates.pas)
async def save_password(message: types.Message, state: FSMContext):
    if await db_set_password(message.chat.id, message.text) == True:
        await message.answer("🟢 Пароль успішно змінено")
        await state.clear()
    else: 
        await message.answer("🟡 Помилка запиту")
        await state.clear()

# @user_router.message(Command("sh_pass"))
# async def show_password(message: types.Message):
#     await message.answer()