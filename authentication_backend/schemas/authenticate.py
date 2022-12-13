from pydantic import BaseModel


class AuthenticateSchema(BaseModel):
    """
    Authenticate schema

    :param user_name: user name
    :param password: password
    """

    user_name: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "user_name": "john",
                "password": "1234"
            }
        }
