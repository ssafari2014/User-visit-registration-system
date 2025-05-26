from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.schemas.visit import PageVisitResponse
from utils.database import get_db
from app.schemas.user import UserCreate, UserOut
from app.services.user import create_page_user
from app.auth.auth_bearer import get_current_user
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache

router = APIRouter(prefix="/user", tags=["Users"])

@router.post("/", response_model=UserOut)
def track_page_user(data: UserCreate, db: Session = Depends(get_db)):
    """ایجاد کاربر جدید در پایگاه داده"""
    return create_page_user(db, data)

@router.get("/me")
@cache(expire=60)
async def get_profile(current_user = Depends(get_current_user)):
    """نمایش اطلاعات کاربر جاری"""
    print("QUERY executed")
    return current_user