from django.conf import settings

from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode

bot = Bot(token=settings.BOT_TOKEN, disable_web_page_preview=True, parse_mode=ParseMode.HTML)

if settings.REDIS_HOST and settings.REDIS_PORT:
    from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
    from redis import Redis

    r = Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=settings.REDIS_DB, decode_responses=True)
    storage = RedisStorage(redis=r, key_builder=DefaultKeyBuilder())
else:
    from aiogram.fsm.storage.memory import MemoryStorage

    storage = MemoryStorage()

dp = Dispatcher()