import redis
from config import REDIS_HOST, REDIS_PORT

# Initialize Redis client
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# Single key-value operations
def create_item(key: str, value: str) -> bool:
    return redis_client.set(key, value)

def get_item(key: str) -> str:
    return redis_client.get(key)

def update_item(key: str, value: str) -> bool:
    return redis_client.set(key, value)

def delete_item(key: str) -> bool:
    return redis_client.delete(key) > 0

# Bulk operations
def create_items(req: dict) -> bool:
    """Creates multiple items. `items` is a dictionary of key-value pairs."""
    return redis_client.mset(req["items"])

def get_items(keys: list) -> dict:
    """Retrieves values for multiple keys. Returns a dictionary of key-value pairs."""
    values = redis_client.mget(keys)
    return dict(zip(keys, values))

def update_items(req: dict) -> bool:
    """Updates multiple items. `items` is a dictionary of key-value pairs."""
    return redis_client.mset(req["items"])

def delete_items(keys: list) -> int:
    """Deletes multiple keys. Returns the number of keys that were deleted."""
    return redis_client.delete(*keys)

def get_all_keys():
    """Retrieve all keys using SCAN"""
    cursor = '0'
    keys = []
    while cursor != 0:
        cursor, next_keys = redis_client.scan(cursor=cursor, match='*', count=100)
        keys.extend(next_keys)
    return keys

def get_all_values():
    """Retrieve values for all keys"""
    print("zzzzzzzzzzz")
    keys = get_all_keys()
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print(keys)
    values = redis_client.mget(keys)
    return dict(zip(keys, values))