from fastapi import APIRouter, Response, status, Cookie, Depends
from app.crud.comment import get_comment, add_comment, delete_comment, update_comment
from app.middleware.auth import get_user

router = APIRouter(
    prefix="/comment",
    tags = ["comment"]
)


@router.get("/{drink_id}", status_code = status.HTTP_200_OK)
async def GetComment(drink_id: str):
    return await get_comment(drink_id)


@router.post("/addcomment/{drink_id}", status_code = status.HTTP_201_CREATED)
async def CreateComment(drink_id: str, text: str):
    return await add_comment(drink_id, text)

@router.delete("/delete/{item_id}", status_code = status.HTTP_200_Ok)
async def DelComment(item_id, user = Depends(get_user)):
    return await delete_comment(item_id, user)