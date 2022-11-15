from jose import JWTError, jwt
from src.config.setup import settings
from src.auth.exceptions import credentials_exception

async def validate_token(token: str):
    try:
        return jwt.decode(token, settings.PROJECT_SECRET_KEY, algorithms=[settings.PROJECT_PROJECT_ALGORITHM])
    except JWTError:
        raise credentials_exception