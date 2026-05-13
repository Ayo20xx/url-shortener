from fastapi import FastAPI
from secrets import token_urlsafe

from app.api import router
from contextlib import asynccontextmanager
from .database.session import create_db_tables



@asynccontextmanager
async def lifespan_handeler(app:FastAPI):
    create_db_tables()
    yield
    


app = FastAPI(
    lifespan= lifespan_handeler
)

app.include_router(router)

def generate_code():
    return token_urlsafe(6)

