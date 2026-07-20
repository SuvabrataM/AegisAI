from app.schemas.common import SuccessResponse


def success_response(message: str, data):
    return SuccessResponse(
        message=message,
        data=data
    )