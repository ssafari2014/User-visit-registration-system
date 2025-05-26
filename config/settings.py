
"""تنظیمات پروژه """
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "User visit registration system"
    DEBUG: bool = False
    DATABASE_URL: str = "sqlite:///database.db"
    SECRET_KEY: str
    VERSION: str = "0.1.0"

    # امنیت
    JWT_SECRET_KEY: str = "supersecret"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

try:
    settings = Settings()
    print("SECRET_KEY:", settings.SECRET_KEY)  # چک کن در ترمینال چاپ بشه
except Exception as e:
    print("⚠️ Settings load error:", e)

