from fastapi import HTTPException, status, Depends
from app.model.drink import Drink
import redis
from app.db import SessionDep

session: SessionDep

redis_client = redis.Redis(host='localhost', port=6379, db=0)

async def get_drink_by_id( item_id: str):
    cached_item = await redis_client.get(f"item_{item_id}")
    if cached_item:
        return {"drink": cached_item.decode('utf-8')}
    
    drink = session.get(Drink, item_id)

    if not drink:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail="Drink not found")

    redis_client.set(f"item_{item_id}", drink)

    return {"drink": drink}

async def get_drink_by_name( name: str):
    drinks = session.exec(select(Drink).where(Drink.name == name))

    if not drinks:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= "Drink not found")

    return {"drinks": drinks}

async def get_drink_by_category( category: str):
    cached_items = await redis_client.get(f"category_{category}")
    if cached_items:
        return {"drinks": cached_item.decode('utf-8')}
    
    drinks = session.exec(select(Drink).where(Drink.category == category))

    if not drinks:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Drink not found")

    redis_client.set(f"category_{category}", drinks)

    return {"drinks": drinks}