import traceback
from fastapi.responses import JSONResponse
from conf import settings


def exception_handler(request, exc):

    if settings.DEBUG:
        traceback.print_exc()

    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal Server Error"
        }
    )
