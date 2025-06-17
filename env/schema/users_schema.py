from pydantic import BaseModel , EmailStr

class New_user_by_id(BaseModel):
    name:str
    email: EmailStr
    is_active: bool = True

    
   