from pydantic import BaseModel


# Модель данных
class Item(BaseModel):
    id: int
    name: str
    price: float

