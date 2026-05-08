from sqlmodel import Field,SQLModel
from pydantic import AnyHttpUrl


class URL(SQLModel,table=True):
    id : int=Field(default=None,primary_key=True)
    url : AnyHttpUrl=Field(unique=True)
    short_code : str 

    

