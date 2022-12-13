from fastapi import (
    status,
    Request,
    Body,
    responses
)
from resources import get_resource
from schemas.verify import VerifySchema


def verify(
    request: Request,
    data: VerifySchema = Body(...),
) -> responses.JSONResponse:
    """
    Verify the integrity of the message
    """
    # get the handle
    method = get_resource('verify')
    # get the response
    # convert the data to a dictionary
    data = data.dict()

    response = method(**data)
    # return the response
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response,
    )
