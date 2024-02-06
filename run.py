from bot_intance import bot
# --- Including all commands functions ---
from bot.handlers.basic import *
from bot.handlers.admin import *
from bot.handlers.linking import *

import asyncio
from aiogram import Dispatcher, types
from aiogram.filters import Command, CommandStart

dp = Dispatcher()

async def main() -> None:
    # -- handling commands ---
    dp.startup.register(startup)
    dp.shutdown.register(shoutdown)
    dp.message.register(start, CommandStart())
    dp.message.register(info, Command('info'))
    dp.message.register(shutbot, Command('shutbot'))
    dp.message.register(set_group, Command('set_group'))
    dp.message.register(remove_group, Command('remove_group'))
    dp.message.register(get_group, Command('group'))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
