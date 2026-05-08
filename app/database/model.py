from sqlmodel import Field,SQLModel,AutoString
from pydantic import AnyHttpUrl


class URL(SQLModel,table=True):
    id : int=Field(default=None,primary_key=True)
    url : AnyHttpUrl = Field(unique=True, sa_type=AutoString) 
    short_code : str 

    

