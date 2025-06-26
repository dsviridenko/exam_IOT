from pydantic import BaseModel
from typing import Optional


class ItemCreate(BaseModel):
    name: str
    price: Optional[float] = 0.0