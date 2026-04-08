from fastapi import FastAPI
from pydantic import BaseModel
from .routers import blog

app = FastAPI()

app.include_router(blog.router)

#class Item(BaseModel):
#    name: str
#    price: float
#    is_offer: bool | None = None
#
#@app.get('/')
#def read_root():
#	return {"Hello": "World"}
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