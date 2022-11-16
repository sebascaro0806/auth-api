from datetime import timedelta
from src.auth.schemas import Introspection, Login, Token, UserProfile, UpdateUserProfile
from fastapi import APIRouter, Request, Depends
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

@auth.get("/user-profile/{id}", response_model=UserProfile)
async def get_user_profile(id: str):
    return service.get_user_profile(id)

@auth.put("/user-profile/{id}", response_model=UserProfile, dependencies=[Depends(dependencies.verify_user_by_id)])
async def update_user_profile(id: str, form_data: UpdateUserProfile):
    return service.update_user_profile(id, form_data)

@auth.get("/validate-token")
async def validate_token(request: Request):
    token_header = request.headers.get('authorization')
    if not token_header:
        raise credentials_exception
    return await dependencies.validate_token(token_header.split(" ")[1])

@auth.post("/introspection")
async def validate_token_post_parametter(token: str):
    if await dependencies.validate_token(token):
        return { "active": True, "tokenstate": True, "tokenstate": { "active": True } }

@auth.post("/introspection2")
async def validate_token_post_data(data: Introspection):
    if await dependencies.validate_token(data.token):
        return { "active": True, "tokenstate": True, "tokenstate": { "active": True } }