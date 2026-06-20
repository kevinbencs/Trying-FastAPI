from pydantic import BaseModel

class CommentSchema(BaseModel):
    text: str