from fastapi import APIRouter,status,HTTPException
from uuid import UUID,uuid4
from schema.users_schema import New_user_by_id
from database import user_db
from models import User
from services.user import user_crud


new_user_router=APIRouter(tags=["new_user"])

@new_user_router.post("/" , status_code= status.HTTP_201_CREATED)
async def new_user(users:New_user_by_id):
   return user_crud.new_user(users)


@new_user_router.get("/", status_code=status.HTTP_200_OK)
async def all_user():
    return user_crud.all_user()


@new_user_router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_user(id:str,users:New_user_by_id):
    return user_crud.update_user(id,users)

    

@new_user_router.delete("/{id}", status_code=status.HTTP_404_NOT_FOUND)
async def remove_user(id:str):
    return user_crud.remove_user(id)
