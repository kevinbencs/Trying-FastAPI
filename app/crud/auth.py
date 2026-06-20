from app.schema.auth import RegisterSchema
from app.config import get_settings
from app.db import get_session
from app.model.user import User
from typing import Annotated
from fastapi import HTTPException, status, Depends
import bcrypt


SessionDep = Annotated[Session, Depends(get_session)]

def SignUp(user: RegisterSchema, session: SessionDep):
    found_user = session.exec(select(User).where(User.email == user.email)).first()

    if found_user:
        return HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email is useb by another account")

    hash_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt()).decode
    db_user = User(name=user.name, password=hash_password, email=user.email)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return {'message': 'success'}