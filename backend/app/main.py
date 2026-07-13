from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logger import setup_logger

logger = setup_logger()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="Enterprise AI Operations Platform",
)

app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX
)


@app.get("/", tags=["Root"])
async def root():
    logger.info("Root endpoint accessed.")

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }