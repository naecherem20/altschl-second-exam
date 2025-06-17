from fastapi import APIRouter, status, HTTPException
from database import event_db
from schema.event_schema import Evention, Evention_upgrade
from services.events import eventers


event_router=APIRouter(tags=["Events"],prefix="/event")

@event_router.get("/",status_code=status.HTTP_200_OK)
async def all_events():
    return eventers.all_events()

@event_router.post("/",status_code=status.HTTP_201_CREATED)
async def new_event(modo:Evention):
    return eventers.new_event(modo)


@event_router.put("/{id}",status_code=status.HTTP_201_CREATED)
async def up_event(id:str,modo:Evention_upgrade):
    return eventers.up_event(id,modo)        

@event_router.delete("/{id}",status_code=status.HTTP_404_NOT_FOUND)
async     def remove_event(id:str):
    return eventers.remove_event(id)