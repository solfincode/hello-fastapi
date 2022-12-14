from typing import Union, Optional
from fastapi import FastAPI
from pydantic import BaseModel

# init app
app = FastAPI()

# init db
db = []


class Item(BaseModel):
    id: int
    title: str
    description: Union[str, None] = None
    body: Union[str, None] = None
    price: int


@app.get("/")
def index():
    return {"msg": "hello world for fastapi"}


@app.post("/create-item")
def create(item: Item):
    db.append(item)
    return item


@app.get("/items")
async def read_item():
    return db


@app.get("/select_item/")
async def select_item(title: str, price: Optional[int] = None):
    selected = []
    for el in db:
        if (title == el.title):
            selected.append(el)
    return selected


@app.get("/items/{id}")
async def get_item(id: int):
    selected = []
    for el in db:
        if (id == el.id):
            selected.append(el)
    return selected


@app.delete("/items/{id}")
async def delete_item(id: int):
    deleted = []
    for el in db:
        if (id == el.id):
            deleted.append(el)
            db.pop(id)
    return {"deleted": deleted}
