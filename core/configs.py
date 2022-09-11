# import os

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação

    para gera o token, foi usando a lib abaixo
    import secrets
    token: str = secrets.token_urlsafe(32)
    """

    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/faculdade"
    DBBaseModel = declarative_base()

    # JWT_SECRET: str = os.environ["JWT_SECRET"]

    JWT_SECRET: str = "jfdkśkfiejfkdjsfoijpdf"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
