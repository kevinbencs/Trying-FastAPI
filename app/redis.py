import redis
import time
from fastapi import FastAPI, Request, HTTPException, Depends

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



async def rate_limiter(request: Request, email: str, max_attempts: int = 5, window: int = 60):
    ip = request.client.host
    key = f"login_rl:{ip}:{email}"

    attempts = await redis_client.incr(key)
    if attempts == 1:
        await redis_client.expire(key, window)

    if attempts > max_attempts:
        ttl = await redis_client.ttl(key)
        raise HTTPException(
            status_code=429,
            detail=f"Too many login attempts. Try again in {ttl} seconds."
        )