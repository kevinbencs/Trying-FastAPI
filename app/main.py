from fastapi import FastAPI
from app.db import create_db_and_tables
from contextlib import asynccontextmanager
from app.routers.auth import router as auth_router
from app.config import get_settings
from app.routers.drink import router as drink_router

settings=get_settings()

@asynccontextmanager
async def lifespan(app:  FastAPI):
    create_db_and_tables()


app = FastAPI(lifespan = lifespan)

app.include_router(auth_router)
app.include_router(drink_router)