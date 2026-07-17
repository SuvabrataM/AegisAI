from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.lifespan import lifespan
from app.core.tags import tags_metadata

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=settings.PROJECT_DESCRIPTION,
    lifespan=lifespan,
    openapi_tags=tags_metadata,
)

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX
)