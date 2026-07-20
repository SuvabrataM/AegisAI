from fastapi import APIRouter

from app.utils.responses import success_response

router = APIRouter(tags=["Health"])


@router.get("/health")
async def health():

    return success_response(
        message="Health check successful",
        data={
            "status": "healthy"
        }
    )