from aiogram import F, Router, types
from bot.data.groupdata import db_condig_emoji

from bot.handlers.user import get_group, remove_group, set_group, web
from bot.utils.texts import *
from bot.keyboards.keyboards import *

callback_router = Router()

async def callbacks(message: types.Message, data: str):
    textfunc = texts[data]
    keyboardfunc = keyboards[data]
    await message.edit_text(text=await textfunc(), reply_markup=await keyboardfunc(), parse_mode='HTML')


@callback_router.callback_query(F.data == "info")
async def call(callback: types.CallbackQuery):
    await callbacks(callback.message, "info")
    await callback.answer()

@callback_router.callback_query(F.data == "menu")
async def call(callback: types.CallbackQuery):
    await callbacks(callback.message, "menu")
    await callback.answer()

@callback_router.callback_query(F.data == "instr")
async def call(callback: types.CallbackQuery):
    await callbacks(callback.message, "instr")
    await callback.answer()

@callback_router.callback_query(F.data == "start")
async def call(callback: types.CallbackQuery):
    await callbacks(callback.message, "start")
    await callback.answer()

@callback_router.callback_query(F.data == "set")
async def call(callback: types.CallbackQuery):
    await set_group(callback.message)
    await callback.answer()

@callback_router.callback_query(F.data == "get")
async def call(callback: types.CallbackQuery):
    await get_group(callback.message)
    await callback.answer()

@callback_router.callback_query(F.data == "web")
async def call(callback: types.CallbackQuery):
    await web(callback.message)
    await callback.answer()

@callback_router.callback_query(F.data == "remove")
async def call(callback: types.CallbackQuery):
    await remove_group(callback.message)
    await callback.answer()

@callback_router.callback_query(F.data == "emoji")
async def call(callback: types.CallbackQuery):
    status = await db_condig_emoji(callback.message.chat.id)
    await callback.message.answer(f"Статус емоджі в вашому чаті змінено на: {status}")
    await callback.answer()

@callback_router.callback_query(F.data == "del")
async def call(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.answer()