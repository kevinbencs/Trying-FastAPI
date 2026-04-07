from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
	return {"Hello": "World"}

@app.get('/item/{item_id}')
def read_item(item_id: int, q: str | None = None):
	return{"item_id": item_id, "q": q}

@app.post('/send/data')
def send_data(item: int):
	print("item: "+str(item))
	return {"message": "success"}