"""پیاده‌سازی وابستگی به احراز هویت"""
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.auth.auth_handler import decode_access_token
from sqlalchemy.orm import Session
from app.models.user import User
from utils.database import get_db
from jose import JWTError


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

"""دریافت کاربر فعلی """
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = db.query(User).filter(User.email == payload.get("sub")).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
