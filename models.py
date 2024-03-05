from pydantic import BaseModel, validator
from typing import List, Dict

class key(BaseModel):
    key: str

class Item(BaseModel):
    key: str
    value: str

class BulkItems(BaseModel):
    items: Dict[str, str]

    @validator('items', each_item=True)
    def check_items(cls, v, values, **kwargs):
        if not isinstance(v, str):
            raise ValueError('Each value must be a string')
        return v

# Alternatively, for more flexibility:
class ItemList(BaseModel):
    items: List[key]