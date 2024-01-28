from aiogram import Bot, types

async def startup(bot: Bot) -> None:
    #await set_commands(bot)
    print("Bot is online")

async def shoutdown(bot: Bot) -> None:
    print("Bot is ofline")