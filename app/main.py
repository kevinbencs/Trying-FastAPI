from fastapi import FastAPI
from app.db import create_db_and_tables
from contextlib import asynccontextmanager

from app.config import get_settings

settings=get_settings()

@asynccontextmanager
async def lifespan(app:  FastAPI):
    create_db_and_tables()


app = FastAPI(lifespan = lifespan)