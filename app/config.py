from pydantic_settings import BaseSettings,SettingsConfigDict

class urlsettings(BaseSettings):
    POSTGRES_SERVER : str
    POSTGRES_PORT : int
    POSTGRES_USER : str
    POSTGRES_PASSWORD : str
    POSTGRES_DB :str 
    BASE_URL : str
    
    model_config= SettingsConfigDict(
        env_file=".env",
        env_ignore_empty = True,
        extra= "ignore"
    )

    def POSTGRES_URL(self):
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
    



settings = urlsettings()
