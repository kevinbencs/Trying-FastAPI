import uuid
from sqlmodel import SQLModel, Field

class Comment(SQLModel, table= True):
    id: uuid.UUID =  Field(default_factory= uuid.uuid4, primary_key = True)
    text: str = Field(index = True)
    email: str = Field(index=True)
    drink_id: uuid.UUID = Field(index = True)