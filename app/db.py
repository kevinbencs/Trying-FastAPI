from sqlmodel import Field, Session, SQLModel, crete_engine
from typing import Annotated
from fastapi import Depends
from app.config import get_settings

settings = get_settings()
engine = create_engine(settings.database_url)

def create_db_and_tables():
    SQLMdel.metada.create_all(engine)

async def get_session():
    with Session(engine) s session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]