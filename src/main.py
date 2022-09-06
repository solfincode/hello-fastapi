from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# init app
app = FastAPI()

# init db
db = []


class Item(BaseModel):
    title: str
    description: Union[str, None] = None
    body: Union[str, None] = None


@app.get("/")
def index():
    return {"msg": "hello world for fastapi"}


@app.post("/create-item")
def create(item: Item):
    db.append(item)
    return item


@app.get("/items")
def read_item():
    return db
