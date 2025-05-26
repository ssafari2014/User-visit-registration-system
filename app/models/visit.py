"""جد ول دیتا بیس بازدید کاربران از صفحات """
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base

class PageVisit(Base):
    """وقتی کاربر از یک صفحه بازدید می‌کند، بازدیدها را می‌دهد
    سریال داده شده برای گزارش ها یا نمودارها
    """
    __tablename__ = "page_visits"

    id = Column(Integer, primary_key=True, index=True)
    page = Column(String,nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    user_agent = Column(String, nullable=False)
