from datetime import timedelta
from src.auth.schemas import Login, Token
from fastapi import APIRouter, Request
import src.auth.service as service
from src.config.setup import settings
from src.auth.exceptions import incorrect_crendentilas_exception, credentials_exception
import src.auth.dependencies as dependencies

auth = APIRouter()

@auth.post("/login", response_model=Token)
async def login(form_data: Login):
    user = service.authenticate_user(form_data.email, form_data.password)
    if not user:
        raise incorrect_crendentilas_exception
    access_token_expires = timedelta(minutes=settings.PROJECT_ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = service.create_access_token(
        data={"sub": user["email"]}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@auth.get("/validate-token")
async def validate_token(request: Request):
    token_header = request.headers.get('authorization')
    if not token_header:
        raise credentials_exception
    return await dependencies.validate_token(token_header.split(" ")[1])