from pydantic import BaseModel, EmailStr

class Register(BaseModel):
    name: str
    email: EmailStr
    password: str

class LogIn(BaseModel):
    email: EmailStr
    password: str