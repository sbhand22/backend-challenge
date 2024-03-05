from huey import RedisHuey
from config import REDIS_HOST, REDIS_PORT
import crud 

# Initialize Huey with Redis backend
huey = RedisHuey('my_app', host=REDIS_HOST, port=REDIS_PORT)


# Single operations
@huey.task()
def create_item_async(key: str, value: str):
    print("Creating item asynchronously with Huey")
    return crud.create_item(key, value)

@huey.task()
def update_item_async(key: str, value: str):
    print("Updating item asynchronously with Huey")
    return crud.update_item(key, value)

@huey.task()
def delete_item_async(key: str):
    print("Deleting item asynchronously with Huey")
    return crud.delete_item(key)

# Bulk operations
@huey.task()
def create_items_async(items: dict):
    print("Creating multiple items asynchronously with Huey")
    return crud.create_items(items)

@huey.task()
def update_items_async(items: dict):
    print("Updating multiple items asynchronously with Huey")
    return crud.update_items(items)

@huey.task()
def delete_items_async(keys: list):
    print("Deleting multiple items asynchronously with Huey")
    return crud.delete_items(keys)

@huey.task()
def get_all_values_async():
    return crud.get_all_values()
