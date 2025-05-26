from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from utils.security import hash_password


def create_page_user(db: Session, user: UserCreate):
    """ایجاد صفحه ثبت نام کاربر """
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pw = hash_password(user.password)
    users = User(name=user.name, email=user.email, hashed_pw=hashed_pw)

    db.add(users)
    db.commit()
    db.refresh(users)
    return users