from fastapi import APIRouter, Response, status, Cookie, Response
from app.schema.auth import RegisterSchema, LogInSchema
from app.crud.auth import SignUp, SignIn, log_out


router = APIRouter(
    prefix = "/auth",
    tags = ['user']
)

@router.post("/register", status_code = status.HTTP_201_CREATED)
async def register(user: RegisterSchema):
    return await SignUp(user)

@router.post("/login", status_code = status.HTTP_200_Ok)
async def login(user: LogInSchema, response: Response):
    return await SignIn(user, response)

@router.get("/logout", status_code = status.HTTP_200_OK)
async def logout(response: Response):
    return await log_out(response)