from fastapi import FastAPI, HTTPException
from models import Item, BulkItems, ItemList 
import crud
from tasks import create_item_async, delete_item_async, update_item_async, create_items_async, update_items_async, delete_items_async
from tasks import huey

app = FastAPI()


# Single operations
@app.post("/item/")
async def create_item(item: Item):
    # Enqueue task for asynchronous execution
    create_item_async(item.key, item.value)
    return {"key": item.key, "value": "Enqueued for creation"}

@app.get("/item/{key}", response_model=Item)
async def read_item(key: str):
    value = crud.get_item(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"key": key, "value": value}

@app.put("/item/{key}")
async def update_item(key: str, item: Item):
    # Enqueue task for asynchronous execution
    update_item_async(key, item.value)
    return {"key": key, "value": "Enqueued for update"}

@app.delete("/item/{key}")
async def delete_item(key: str):
    # Enqueue task for asynchronous execution
    delete_item_async(key)
    return {"detail": "Enqueued for deletion"}

# Bulk operations
@app.post("/items/bulk/create")
async def create_items_bulk(items: BulkItems):
    # Enqueue bulk create task for asynchronous execution
    create_items_async(items.dict())
    return {"detail": "Bulk create enqueued"}

@app.put("/items/bulk/update")
async def update_items_bulk(items: BulkItems):
    # Enqueue bulk update task for asynchronous execution
    update_items_async(items.dict())
    return {"detail": "Bulk update enqueued"}

@app.delete("/items/bulk/delete")
async def delete_items_bulk(item_list: ItemList):
    # Enqueue bulk delete task for asynchronous execution
    keys = [item.key for item in item_list.items]
    delete_items_async(keys)
    return {"detail": "Bulk delete enqueued"}

@app.get("/items/all")
async def read_all_items():
    # print("zzzzzzzzzhere")
    items = crud.get_all_values()
    if not items:
        raise HTTPException(status_code=404, detail="No items found")
    return items
