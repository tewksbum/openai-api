from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

class ItemCreate(BaseModel):
    name: str
    description: str
    price: float

class Item(ItemCreate):
    id: int

router = APIRouter()

@router.get("/items/", response_model=List([Item]))
async def get_items():
    # fetch items from db
    items = []
    return items

@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    # fetch items from db
    item = None

    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')
    return item