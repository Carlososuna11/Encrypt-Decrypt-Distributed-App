from pydantic import BaseModel


class VerifySchema(BaseModel):

    text_to_verify: str
    text_to_verify_hash: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "text_to_verify": "john",
                "text_to_verify_hash": "jasklaksl",
                "password": "1234"
            }
        }
