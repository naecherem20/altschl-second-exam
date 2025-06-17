from pydantic import EmailStr
class User:
    def __init__(self, id: str , name: str, email: EmailStr, is_active: bool = True):
        self.id=id
        self.name=name
        self.email= email
        self.is_active= is_active
class Register:
    def __init__(self, id: str , user_id: str, event_id:int, registration_date: str,attended: bool = False):
        self.id=id
        self.user_id=user_id
        self.event_id= event_id
        self.attended= attended
        self.registration_date=registration_date
class Event:
    def __init__(self, id: str , title: str, location:int, event_date: str,is_open: bool = True):
        self.id=id
        self.title=title
        self.location= location
        self.event_date=event_date
        self.is_open= is_open