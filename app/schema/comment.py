from pydantic import BaseModel, EmailStr

class CommentSchema(BaseModel):
    text: str | None = None
    email: EmailStr| None = None
    drink_id: str | None = None