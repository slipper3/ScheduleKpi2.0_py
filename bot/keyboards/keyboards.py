from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, KeyboardButtonPollType, InlineKeyboardButton, InlineKeyboardMarkup

# --- This file contains all keyboards ---

async def start_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="⚙️ Меню", callback_data='menu')],
            [InlineKeyboardButton(text="🌀 Додатков інформація", callback_data='info')],
            [InlineKeyboardButton(text="💢 Прибрати повідомлення", callback_data='del')]
        ])

async def menu_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='📌 Прикріпити групу', callback_data='set'),
            InlineKeyboardButton(text='🔗 Посилання на сайт', callback_data='web')],
            [InlineKeyboardButton(text='🔎 Переглянути групу', callback_data='get'),
            InlineKeyboardButton(text='🔇 Відкріпити групу', callback_data='remove')],
            [InlineKeyboardButton(text='😇 Налаштувати стікери',  callback_data='emoji'),
            InlineKeyboardButton(text='📖 Інструкція', callback_data='instr')],
            [InlineKeyboardButton(text="◀️ Назад", callback_data='start')]
        ], resize_keyboard=True)

async def info_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="◀️ Назад", callback_data='start')]
        ])

async def instr_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="◀️ Назад", callback_data='menu')]
        ])

keyboards = {
    "start": start_keyboard,
    "menu": menu_keyboard,
    "info":  info_keyboard,
    "instr": instr_keyboard
}

