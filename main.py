from fastapi import FastAPI
from routes.user_router import new_user_router
from routes.registration_router import registration_router
from routes.event_router import event_router



app=FastAPI()
app.include_router(new_user_router)
app.include_router(registration_router)
app.include_router(event_router)

