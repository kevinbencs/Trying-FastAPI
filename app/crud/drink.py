from fastapi import HTTPException, status, Depends
from app.model.drink import Drink

from app.db import SessionDep

async def get_drink_by_id(session: SessionDep, item_id: str):
    drink = session.get(Drink, item_id)

    if not drink:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Drink not found")

    return {"drink": drink}

async def get_drink_by_name(session: SessionDep, name: str):
    drinks = session.exec(select(Drink).where(Drink.name == name))

    if not drinks:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Drink not found")

    return {"drinks": drinks}