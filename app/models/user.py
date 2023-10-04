from pydantic import BaseModel,Field,EmailStr
from datetime import datetime, timedelta

class User(BaseModel):
    name:str=Field(default=None)
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)
    
class UserLogin(BaseModel):
    email:EmailStr=Field(default=None)
    password:str=Field(default=None)

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str

class changepassword(BaseModel):
    email:str
    old_password:str
    new_password:str

class TokenCreate(BaseModel):
    user_id:str
    access_token:str
    refresh_token:str
    status:bool
    created_date:datetime