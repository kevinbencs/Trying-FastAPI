from fastapi import APIRouter, Response, status
from app.crud.drink import get_drink_by_id, get_drink_by_category, get_drink_by_name


router = APIRouter(
    prefix= "/drink",
    tags=["drink"]
)

@router.get("/drink/id/{item_id}", status_code = status.HTTP_200_Ok)
async def GetDrinkById(item_id: str):
    return await get_drink_by_id(item_id)

@router.get("/drink/category/{category}", status_code = status.HTTP_200_Ok)
async def GetDrinkByCat(category: str):
    return await get_drink_by_category(category)

@router.get("/drink/search", status_code = status.HTTP_200_Ok)
async def GetDrinkByName(name: str):
    return await get_drink_by_name(name)