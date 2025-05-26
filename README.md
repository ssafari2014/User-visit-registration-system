                                                                                                                                                                                                                                                                             🚀 User Visit Tracking System (FastAPI + Redis Cache + Docker)
سیستمی حرفه‌ای برای ثبت و مدیریت بازدیدهای کاربران با استفاده از FastAPI، کش حرفه‌ای با Redis و استقرار آسان با Docker.

🧠 درباره پروژه
این پروژه یک API حرفه‌ای برای ثبت و بررسی بازدیدهای کاربران ارائه می‌دهد. برای افزایش کارایی، داده‌های بازدید با استفاده از Redis کش می‌شوند تا از اجرای Queryهای غیرضروری جلوگیری شود.

🔧 تکنولوژی‌ها و ابزارها
🐍 Python 3.12

⚡ FastAPI

🛢 PostgreSQL / SQLite (پیش‌فرض)

🚀 Redis (برای کش)

🐳 Docker + Docker Compose

🔐 JWT (برای احراز هویت)

📦 Uvicorn (سرور ASGI)

📂 ساختار پروژه
.
├── app/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   └── services/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


⚙️ نحوه اجرا با Docker

docker-compose up --build
پس از اجرا:

اپلیکیشن در آدرس: http://localhost:8000

مستندات OpenAPI: http://localhost:8000/docs

🧪 تست سریع با Postman
🧠 قابلیت‌ها
ثبت‌نام و لاگین کاربران با JWT

کش اطلاعات بازدید کاربران با Redis

ساختار ماژولار و تمیز برای توسعه راحت‌تر

داکرایز کامل برای اجرا در هر محیطی


🧰 دستورات مفید

# ساخت requirements.txt
pip freeze > requirements.txt

# اجرا در محیط توسعه
uvicorn main:app --reload

# بررسی Redis در CLI
docker exec -it redis_container redis-cli

👨‍💻 توسعه‌دهنده
سجاد صفری 
Email : s.saffari2014@yahoo.com
github : https://github.com/ssafari2014/
linkdin : https://www.linkdin.com/in/sajjad-sa-64b1431b4/



