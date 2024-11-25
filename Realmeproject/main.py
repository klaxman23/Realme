from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Define a data model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory storage for items
items = []

# GET operation to read all items
@app.get("/items/", response_model=List[Item])
def read_items():
    return items

# GET operation to read a single item by ID
@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# POST operation to create a new item
@app.post("/items/", response_model=Item)
def create_item(item: Item):
    items.append(item)
    return item

# PUT operation to update an existing item
@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item.id == item_id:
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

# DELETE operation to remove an item by ID
@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            return items.pop(index)
    raise HTTPException(status_code=404, detail="Item not found")
