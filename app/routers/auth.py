from fastapi import APIRouter, Response, status, Cookie
from app.schema.auth import RegisterSchema
from app.crud.auth import SignUp


router = APIRouter(
    prefix = "/auth",
    tags = ['user']
)

@router.post("/register", status_code = status.HTTP_201_CREATED)
async def register(user: RegisterSchema):
    return await SignUp(user)