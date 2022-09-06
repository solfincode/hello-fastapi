from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"msg": "hello world for fastapi"}
