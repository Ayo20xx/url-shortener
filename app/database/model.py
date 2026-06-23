from datetime import datetime, timezone

from sqlmodel import Field,SQLModel,AutoString
from pydantic import AnyHttpUrl


class URL(SQLModel,table=True):
    id : int=Field(default=None,primary_key=True)
    url : AnyHttpUrl = Field(unique=True, sa_type=AutoString) 
    short_code : str 
    click_count: int = Field(default=0)
    created_at: datetime = Field(default_factory=lambda:datetime.now(timezone.utc))

    

