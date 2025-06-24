from pydantic import BaseModel


class Registration(BaseModel):

    id: int
    name: str
    topic: str