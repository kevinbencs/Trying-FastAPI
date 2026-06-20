from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class LogInSchema(BaseModel):
    email: EmailStr
    password: str