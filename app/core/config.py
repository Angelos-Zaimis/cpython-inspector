from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "CPython Inspector"
    APP_VERSION: str = "0.1.0"
    APP_DESCRIPTION: str = "A deep inspection tool for CPython internals — disassemble"
    DEBUG: bool = True
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
