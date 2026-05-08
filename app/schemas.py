from pydantic import BaseModel,AnyHttpUrl




class Url(BaseModel):
    url : AnyHttpUrl

