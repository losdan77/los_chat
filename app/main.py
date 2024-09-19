from fastapi import FastAPI

from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis

from app.config import settings
from app.users.router import router as router_auth
from app.chats.router import router as router_chats
from app.messages.router import router as router_messages


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(f"redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}")
    FastAPICache.init(RedisBackend(redis), prefix="cache")
    yield

app = FastAPI(title='Los_chat', lifespan=lifespan)

app.include_router(router_auth)
app.include_router(router_chats)
app.include_router(router_messages)
