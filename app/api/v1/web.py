from fastapi import APIRouter, HTTPException, status
from typing import List
from app.schemas.item import Item
from app.models.item import ItemCreate

# "База данных"
items_db = [
    Item(id=1, name="Item 1", price=10.0),
    Item(id=2, name="Item 2", price=20.0)
]
next_id = 3

router = APIRouter()

@router.get("/", summary="Корневая страница")
def read_root():
    return {"message": "Welcome to FastAPI REST Server"}


@router.get("/items", response_model=List[Item], summary="Получить все элементы")
def read_items():
    return items_db


@router.get("/items/{item_id}", response_model=Item, summary="Получить элемент по ID")
def read_item(item_id: int):
    item = next((i for i in items_db if i.id == item_id), None)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items", response_model=Item,
          status_code=status.HTTP_201_CREATED,
          summary="Создать новый элемент")
def create_item(item: ItemCreate):
    global next_id
    new_item = Item(id=next_id, name=item.name, price=item.price)
    items_db.append(new_item)
    next_id += 1
    return new_item


@router.delete("/items/{item_id}", status_code=204, summary="Удалить элемент")
def delete_item(item_id: int):
    global items_db
    initial_length = len(items_db)
    items_db = [item for item in items_db if item.id != item_id]

    if len(items_db) == initial_length:
        raise HTTPException(status_code=404, detail="Item not found")
    return

