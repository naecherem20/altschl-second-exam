from fastapi import APIRouter,status,HTTPException
from uuid import UUID,uuid4
from schema.users_schema import New_user_by_id
from database import user_db



class UserCrud:
    @staticmethod
    def new_user(users:New_user_by_id):
        user_id=uuid4()
    
        users={"id":user_id, **users.model_dump()}
        user_db.append(users)
        return{"New_users_by_id":users}
    
    @staticmethod
    def all_user():
        return{"All_users":user_db}

    @staticmethod
    def update_user(id:str,users:New_user_by_id):
    
        for i, u in enumerate(user_db):
            if str(u["id"]) == id:
                updated_user = users.model_dump()
                updated_user["id"] = id  
                user_db[i] = updated_user
                return updated_user
        
        raise HTTPException(status_code=404 )
    @staticmethod
    def remove_user(id:str):
        try:
            for u in user_db:
                if str(u["id"]) == id:
                    user_db.remove(u)
                    return {"message":"Deleted successfully!!" }
        except:
            return {"error": "User not found"}

            


    

user_crud = UserCrud()

