from fastapi import HTTPException, status
from app.model.comment import Comment
from app.db import SessionDep
from app.model.user import User
from app.schema.comment import CommentSchema

async def get_comment(session: SessionDep, drink_id: str):
    comments = session.exec(select(Comment).where(Comment.drink_id == drink_id))

    if not comments:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Comment not found")

    return {"comments": comments}

async def add_comment(session: SessionDep, drink_id: str, user: User, text: str):
    if not text:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail = "Text is required.")
    db_comment = Comment(text = text, email = user.email, drink_id = drink_id)
    session.add(db_comment)
    session.commit()
    session.refresh(db_comment)

    return {"message": "success"}

async def update_comment(session: SessionDep, comment_id: str, comment: CommentSchema):
    if not comment:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail= "Text is required ")

    db_comment = session.get(Comment, comment_id)

    if not db_comment:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= "Comment not found")

    comment_data = comment.model_dump(exclude_unset = True)
    db_comment.sqlmodel_update(comment_data)
    session.add(db_comment)
    session.commit()
    session.refresh(db_comment)

    return {"message": "success"}


async def delete_comment(session: SessionDep, id: str):
    comment = session.get(Comment, id)

    if not comment:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUD, detail = "Comment not found")

    session.delete(comment)
    session.commit()

    return {"message": "success"}