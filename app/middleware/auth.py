from fastapi import Depends, HTTPException, status, Cookie
from typing import Annotated
import jwt
from app.config import get_settings
from app.db import SessionDep
from app.model.user import User

settings = get_settings()

SECRET = settings.jwt_secret
ALGORITHM = settings.jwt_algorithm
session: SessionDep


async def get_user(authsession: Annotated[str | None, Cookie()] = None):
    if authsession is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Please log in")

    try:
        payload = jwt.decode(authsession, SECRET, algorithms=[ALGORITHM])
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Session expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invaid token")

    user_id = payload.get("user_id")

    if user_id is None:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "Invalid token payload")

    user = session.get(User, user_id)
    return user