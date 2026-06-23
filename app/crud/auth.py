from app.schema.auth import RegisterSchema, LogInSchema
from app.config import get_settings
from app.db import  SessionDep
from app.model.user import User
from typing import Annotated
from fastapi import HTTPException, status, Depends, Response
import bcrypt
import jwt


settings = get_settings
SECRET = settings.jwt_secret
ALGORITHM = settings.jwt_algorithm
EXPIRE = settings.jwt_expire_minutes



async def SignUp(user: RegisterSchema, session: SessionDep):
    found_user = session.exec(select(User).where(User.email == user.email)).first()

    if found_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is useb by another account")

    hash_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode
    db_user = User(name=user.name, password=hash_password, email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return {'message': 'success'}


async def SignIn(user: LogInSchema, session: SessionDep, response: Response):
    found_user = session.exec(select(User).where(user.email == User.email)).first()

    if not found_user or bcrypt.checkpw(user.password.encode(), found_user.password.encode()):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Invalid email or password')

    expire = datetime.utcnow() + timedelta(minutes=EXPIRE)
    token = jwt.encode({"user_id": found_user.id, 'exp': expire}, SECRET, algorithms = ALGORITHM)
    response.set_cookie(key='authsession', value=token, secure = True, httponly = True, expires=EXPIRE)
    return {"message": "success"}


async def log_out(response: Response):
    response.delete_cookie('authsession')

    return {"message": "success"}