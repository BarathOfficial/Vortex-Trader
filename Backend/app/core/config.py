# config.py
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List

class Settings(BaseSettings):
    
    DATABASE_URL: str

    MARKETAUX_APIKEY: str
    MARKETAUX_BASE_USRL: str



    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()
   