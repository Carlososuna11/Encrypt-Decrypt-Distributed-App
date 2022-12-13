from fastapi import (
    status,
    Request,
    Body,
    responses
)
from resources import get_resource
from schemas.signature import SignatureSchema


def signature(
    request: Request,
    data: SignatureSchema = Body(...),
) -> responses.JSONResponse:
    """
    signature the message
    """
    # get the handle
    method = get_resource('signature')
    # get the response
    # convert the data to a dictionary
    data = data.dict()

    response = method(**data)
    # return the response
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response,
    )
