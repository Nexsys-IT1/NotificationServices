from fastapi import FastAPI
from routers.notification_router import router

app = FastAPI()

app.include_router(router, prefix="/notifications")
