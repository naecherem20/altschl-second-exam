from database import event_db
from schema.event_schema import Evention, Evention_upgrade
from fastapi import  HTTPException


class Eve:
    @staticmethod
    def all_events():
        return event_db
    
    @staticmethod
    def new_event(modo:Evention):
        modo=(modo.model_dump())
        event_db.append(modo)
        return modo

    @staticmethod
    def up_event(id:str,modo:Evention_upgrade):
        for index,i in enumerate(event_db):
            if i.get("id")==id:
                upgrade_event=modo.model_dump()
                upgrade_event["id"]=id
                event_db[index]=upgrade_event
                return upgrade_event
        raise HTTPException(status_code=404, detail="event has not been registered")
            
    @staticmethod
    def remove_event(id:str):
        for i in event_db:
            if i["id"]==id:
                event_db.remove(i)
                return("deleted successfully!!")
        return ("this user does not exist")
        




eventers=Eve()