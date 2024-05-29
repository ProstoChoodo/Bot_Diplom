from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault
from .CommandNames import *


commands = [
    BotCommand(command=f"/command", description="description"),
]


async def set_default_commands(bot: Bot):
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())
    