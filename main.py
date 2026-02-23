import asyncio
import sys
from dotenv import load_dotenv

load_dotenv()

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

from fastapi import FastAPI
from api.notification_router import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8080",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://insurance-client-react-dev-d2b0e3azbncyapcp.centralindia-01.azurewebsites.net",
        'https://protego2.nexsysit.co.in',
        'https://protego2admin.nexsysit.co.in'
    ],
    allow_credentials=True,  # IMPORTANT for SSE
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)
 
app.include_router(router, prefix="/notifications")
