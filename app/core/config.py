from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ORIGINS: str
    class Config:
        env_file = ".env"


settings = Settings()
