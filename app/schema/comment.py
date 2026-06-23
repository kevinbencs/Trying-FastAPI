from pydantic import BaseModel

class CommentSchema(BaseModel):
    text: str | None = None
    email: str | None = None
    drink_id: str | None = None