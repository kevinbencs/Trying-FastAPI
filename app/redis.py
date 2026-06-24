import redis

async def init_redis():
    global redis
    redis_client = redis.Redis(host='localhost', port=6379, db=0)

async def close_redis():
    global redis
    if redis:
        await redis.close()



async def get_cache(key: str):
    if not redis:
        raise RuntimeError("Redis not initialized. Call init_redis() first.")
    return await redis.get(key)

async def set_cache(key: str, value: str, ttl: int = 300):
    if not redis:
        raise RuntimeError("Redis not initialized. Call init_redis() first.")
    await redis.set(key, value, ex=ttl)

async def delete_cache(key: str):
    if not redis:
        raise RuntimeError("Redis not initialized. Call init_redis() first.")
    await redis.delete(key)