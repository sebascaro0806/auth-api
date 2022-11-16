from jose import JWTError, jwt
from src.config.setup import settings
from src.auth.service import get_user_profile
from src.auth.exceptions import credentials_exception, user_not_found_exception

async def validate_token(token: str):
    try:
        return jwt.decode(token, settings.PROJECT_SECRET_KEY, algorithms=[settings.PROJECT_PROJECT_ALGORITHM])
    except JWTError:
        raise credentials_exception

def verify_user_by_id(id):
    if not get_user_profile(id):
        raise user_not_found_exception
    return True