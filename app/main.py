from fastapi import FastAPI
from app.db import create_db_and_tables
from contextlib import asynccontextmanager
from app.routers.auth import router as auth_router
from app.config import get_settings
from app.routers.drink import router as drink_router
from app.routers.comment import router as comment_router
from app.redis import init_redis, close_redis


settings=get_settings()

@asynccontextmanager
async def lifespan(app:  FastAPI):
    create_db_and_tables()
    await init_redis()
    yield
    await close_redis()


app = FastAPI(lifespan = lifespan)

app.include_router(auth_router)
app.include_router(drink_router)
app.include_router(comment_router)