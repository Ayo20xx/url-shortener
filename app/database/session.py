from sqlmodel import Session,SQLModel
from fastapi  import Depends
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlmodel.ext.asyncio.session import AsyncSession
from typing import Annotated
from app.config import settings
engine=create_async_engine(
        url=settings.DATABASE_URL,
        echo= True,
        )

async def create_db_tables():
    async with engine.begin() as connection:
        from .model import URL # noqa: F401
        await connection.run_sync(SQLModel.metadata.create_all)

async def get_session():
    async_session= async_sessionmaker(
        bind= engine,
        class_=AsyncSession,
        expire_on_commit= False,
    )



    async with async_session() as session:
        yield session

SessionDep=Annotated[Session,Depends(get_session)]