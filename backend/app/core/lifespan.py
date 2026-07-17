from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.core.logger import setup_logger

logger = setup_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Aegis AI...")

    # Future:
    # Connect PostgreSQL
    # Connect Qdrant
    # Load ML Models
    # Initialize Cache

    yield

    logger.info("Shutting down Aegis AI...")

    # Future:
    # Close DB Connections
    # Flush Logs
    # Cleanup Resources