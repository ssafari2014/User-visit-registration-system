from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password):
    """هش کردن پسورد"""
    return pwd_context.hash(password)
def verify_password(plain_password, hashed_password):
    """تأیید رمز عبور در برابر هش"""
    return pwd_context.verify(plain_password, hashed_password)

