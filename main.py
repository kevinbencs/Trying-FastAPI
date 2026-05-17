from typing import Annotated
from fastapi import FastAPI, Form, HTTPException, Cookie, Response
from pydantic import BaseModel
from .routers import blog, book

app = FastAPI()

app.include_router(blog.router)

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

class Cookies(BaseModel):
    session_id: str
    name: str | None = None
    token: str | None = None


@app.get('/')
def read_root():
	return {"Hello": "World"}
#
#@app.get('/item/{item_id}')
#def read_item(item_id: int, q: str | None = None):
#	return{"item_id": item_id, "q": q}
#
#@app.post('/send/data')
#def send_data(item: int):
#	print("item: "+str(item))
#	return {"message": "success"}
#
#
#
#@app.put("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#    return {"item_name": item.name, "item_id": item_id}

@app.post("/register/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()], status_code=201):
    return {"message": "Success"}

@app.post("/cookie-and-object/")
def create_cookie(response: Response, status_code=201):
    response.set_cookie(key="fakesession", value="fake-cookie-session-value")
    return {"message": "Come to the dark side, we have cookies"}