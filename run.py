from bot_intance import bot
# --- Including all routers ---
from bot.handlers.admin import admin_router
from bot.handlers.user import user_router

import asyncio
from aiogram import Dispatcher


async def register_routers(dp: Dispatcher) -> None:
    """ Including routers to the main dispatcher """
    dp.include_router(admin_router)
    dp.include_router(user_router)


async def main() -> None:
    """ Starting bot """

    dp = Dispatcher()
    await register_routers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    

if __name__ == "__main__":
    asyncio.run(main())
