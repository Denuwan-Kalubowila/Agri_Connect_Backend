from fastapi import APIRouter,Depends, HTTPException,status
from models.user import User,UserLogin
from config.database import collection
from schema.schemas import list_serial_list
from bson import ObjectId
from typing import List
from utils import get_hashed_password,verify_password,create_access_token,create_refresh_token
from models.user import TokenSchema

router=APIRouter()



#add user
@router.post('/login' ,response_model=TokenSchema)
def login(request:UserLogin):
    user = db.query(User).filter(User.email == request.email).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect email")
    hashed_pass = user.password
    if not verify_password(request.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password"
        )
    
    access=create_access_token(user.id)
    refresh = create_refresh_token(user.id)

    token_db = models.TokenTable(user_id=user.id,  access_toke=access,  refresh_toke=refresh, status=True)
    db.add(token_db)
    db.commit()
    db.refresh(token_db)
    return {
        "access_token": access,
        "refresh_token": refresh,
    }
