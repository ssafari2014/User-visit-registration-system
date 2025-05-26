from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from app.routers import user
from app.routers import visit
from app.routers import auth

from redis import asyncio as aioredis
app = FastAPI()

@app.on_event("startup")
async def startup():
    redis = aioredis.from_url(
        "redis://redis:6379",  # بدون http یا چیزی اضافه
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")


# ثبت کردن روت‌ها
app.include_router(user.router)
app.include_router(visit.router)
app.include_router(auth.router)





if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
