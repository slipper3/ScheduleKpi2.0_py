from bot_intance import bot
# --- Including all routers ---
from bot.handlers.admin import admin_router
from bot.handlers.user import user_router

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from bot.utils.apschedule import schedul

import asyncio
from aiogram import Dispatcher


async def register_routers(dp: Dispatcher) -> None:
    """ Including routers to the main dispatcher """
    dp.include_router(admin_router)
    dp.include_router(user_router)


async def main() -> None:
    """ Starting bot """
    # register scheduls
    sched = AsyncIOScheduler()
    sched.add_job(schedul, 'cron', hour=8, minute=25, args=['8:30', bot])
    sched.add_job(schedul, 'cron', hour=10, minute=20, args=['10:25', bot])
    sched.add_job(schedul, 'cron', hour=12, minute=15, args=['12:20', bot])
    sched.add_job(schedul, 'cron', hour=14, minute=10, args=['14:15', bot])
    sched.add_job(schedul, 'cron', hour=16, minute=5, args=['16:10', bot])
    sched.add_job(schedul, 'cron', hour=18, minute=25, args=['18:30', bot])

    dp = Dispatcher()
    await register_routers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
    

if __name__ == "__main__":
    asyncio.run(main())
