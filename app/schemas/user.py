"""
UserCreate and UserOut
"""
from pydantic import BaseModel, EmailStr
from pydantic import ConfigDict


class UserCreate(BaseModel):
    """داده هایی که کاربر هنگام ثبت نام می‌فرسته"""
    name: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    """داده‌هایی که بعد از ثبت نام یا لاگین به کاربر نمایش داده می‌شوند"""
    id : int
    name: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)

