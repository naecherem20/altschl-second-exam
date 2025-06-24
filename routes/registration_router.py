from fastapi import APIRouter, status, HTTPException
from uuid import UUID,uuid4
from schema.register_schema import Registration
from database import register_db,user_db ,event_db
from services.register import user_registers

registration_router=APIRouter(tags=["registration"],prefix="/register")

@registration_router.get("/" , status_code=status.HTTP_200_OK)
async def all_registered():
    return user_registers.all_registered()

                
@registration_router.post("/event",status_code= status.HTTP_201_CREATED)
async def new_signup(signup:Registration):
    return user_registers.new_signup(signup)


@registration_router.post("/{registered_id}",status_code= status.HTTP_201_CREATED)
async def sign_ups_by_id(registered_id:str):
    return user_registers.sign_ups_by_id(registered_id)

 
@registration_router.get("/attendance",status_code=status.HTTP_200_OK)
async def attendance():
    return user_registers.attendance()


       
       