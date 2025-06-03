print(">>> main.py is loaded <<<")

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.get("/items")
async def items():
    return {"message": "You are in items"}

@app.get("/")
async def root():
    return {"message": "Hello world"}
