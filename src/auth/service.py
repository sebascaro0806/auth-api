from datetime import datetime, timedelta
from typing import Union

from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from src.config.setup import settings

from src.config.db import engine
from src.auth.models import users

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except:
        return False

def authenticate_user(email: str, password: str):
    user = get_user(email)
    print(user)
    if not user:
        return False
    if not verify_password(password, user["password"]):
        return False
    return user

def get_user(email: str):
    with engine.connect() as conn:
        return conn.execute(users.select().where(users.c.email == email)).first()

def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.PROJECT_SECRET_KEY , algorithm=settings.PROJECT_PROJECT_ALGORITHM)
    return encoded_jwt

