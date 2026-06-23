from typing import Optional

from pydantic_settings import BaseSettings,SettingsConfigDict

class urlsettings(BaseSettings):
    DATABASE_URL :str
    BASE_URL: Optional[str] = None
    
    model_config= SettingsConfigDict(
        env_file=".env",
        env_ignore_empty = True,
        extra= "ignore"
    )

 

settings = urlsettings()
