from pydantic import BaseModel


class AuthenticateSchema(BaseModel):

    user_name: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "user_name": "john",
                "password": "1234"
            }
        }
