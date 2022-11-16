from pydantic import BaseModel
from typing import Union

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Union[str, None] = None

class Login(BaseModel):
    email: str
    password: str

class UserProfile(BaseModel):
    email: str
    first_name: str
    last_name: str
    photo: str

class UpdateUserProfile(BaseModel):
    first_name: str
    last_name: str
    photo: str
    password: str

class Introspection(BaseModel):
    token: str