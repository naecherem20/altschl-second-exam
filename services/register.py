from schema.event_schema import Evention, Evention_upgrade
from schema.register_schema import Registration
from database import register_db,user_db ,event_db
from fastapi import APIRouter, status, HTTPException



class Registrars:
    @staticmethod
    def all_registered():
        return (register_db)


    @staticmethod
    def new_signup(signup:Registration):
   
        signup= signup.model_dump()
    
        open_event=True

        
        for e in event_db:
            if e.get("is_open") is True:
                open_event=e
                break
            if open_event is False:
                raise HTTPException(status_code=404, detail="No open events available")
        for user in user_db:
            if str(user.get("id")) == str(signup["user_id"]):
                if user.get("is_active") == True:
                    signup["user_id"]= str(user.get("id"))
                    break
                else:
                    raise HTTPException(status_code=404, detail="user doesnt exist or is not active")
        
        for r in register_db:
            if r.get("user_id")== signup.get("user_id"):
                return("this user has been registered")
        register_db.append(signup)
        return ("Registration successful!!")
            
    @staticmethod
    def sign_ups_by_id(registered_id:str):
        for regs in register_db:
            if regs.get("user_id")==registered_id:
                return (regs)
        
        raise HTTPException(status_code=404, detail="user doesnt exist or is not active")
    
    @staticmethod
    def attendance():
        attended_users=[regs for regs in register_db if regs.get("attended") == True]
        if attended_users:
            return (attended_users)
        
        raise HTTPException(status_code=404, detail="no attended user found")
                    

    



user_registers=Registrars()