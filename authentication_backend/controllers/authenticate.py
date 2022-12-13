from fastapi import (
    status,
    Request,
    Body,
    responses
)
from resources import get_resource
from schemas.authenticate import AuthenticateSchema


def authenticate(
    request: Request,
    data: AuthenticateSchema = Body(...),
) -> responses.JSONResponse:
    """
    Authenticate the user
    """

    method = get_resource('authenticate')

    # get the response
    # convert the data to a dictionary
    data = data.dict()

    response = method(**data)
    # return the response
    return responses.JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response,
    )
