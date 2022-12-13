from pydantic import BaseModel


class SignatureSchema(BaseModel):
    """
    Signature schema

    :param text_to_encrypt: text to encrypt
    :param user_name: user name
    """

    text_to_encrypt: str
    user_name: str

    class Config:
        schema_extra = {
            "example": {
                "text_to_encrypt": "hello world",
                "user_name": "john"
            }
        }
