from fastapi import HTTPException, status
from app.model.comment import Comment
from app.db import SessionDep
from app.model.user import User


async def get_comment(session: SessionDep, drink_id: str):
    comments = session.exec(select(Comment).where(Comment.drink_id == drink_id))

    if not comments:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Comment not found")

    return {"comments": comments}

async def add_comment(session: SessionDep, drink_id: str, user: User, text: str):
    db_comment= Comment(text = text, email = user.email, drink_id = drink_id)
    session.add(db_comment)
    session.commit
    session.refresh(db_comment)

    return {"message": "success"}