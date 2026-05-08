from sqlmodel import Session,SQLModel
from fastapi  import Depends
from sqlalchemy import create_engine
from typing import Annotated

engine=create_engine(
        url="sqlite:///sqlite.db",
        echo= True,
        connect_args={"check_same_thread":False}
        )

def create_db_tables():
    from .model import URL # noqa: F401
    SQLModel.metadata.create_all(bind=engine)

def get_session():
    with Session(bind=engine) as session:
        yield session
SessionDep=Annotated[Session,Depends(get_session)]