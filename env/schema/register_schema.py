
from pydantic import BaseModel


class Registration(BaseModel):
    id: int
    user_id: str
    event_id: int
    registration_date: str
    attended: bool = False
