from fastapi import FastAPI
from uvicorn import Config, Server

from api.v1.api import api_router
from core.configs import settings
from logging_config import LOG_LEVEL, setup_logging

app = FastAPI(title="Curso API - Segurança")
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    server = Server(
        Config(
            "main:app",
            host="localhost",
            log_level=LOG_LEVEL,
        ),
    )

    setup_logging()

    server.run()
