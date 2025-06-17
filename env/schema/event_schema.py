from pydantic import BaseModel , EmailStr, Field
from datetime import date

class Evention(BaseModel):
    id: str
    title: str
    location: str
    event_date: date
    is_open: bool=True

class Evention_upgrade(BaseModel):
    title: str
    location: str
    event_date: date
    is_open: bool=True