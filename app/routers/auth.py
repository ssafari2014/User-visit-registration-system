"""مسیر ورود """
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.auth.auth_handler import create_access_token
from utils.security import verify_password
from app.models.user import User
from utils.database import get_db

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user  = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_pw):
        raise HTTPException(status_code=401, detail="Incorrect credentials")
    access_token = create_access_token(data={"sub": user.email})
    print("access_token : ", access_token)
    return {"access_token": access_token, "token_type": "bearer"}