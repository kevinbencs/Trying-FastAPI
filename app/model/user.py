from sqlmodel import SQModel, Field
import uuid

class User(SQModel, table = True):
    id: uuid.UUID = Field(default_factory = uuid.uuid4, primary_key= True)
    name: str = Field(index = True)
    password: str
    email: str = Field(index = True)