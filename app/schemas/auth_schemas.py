from pydantic import BaseModel, EmailStr
from utils.validators import EmailValidator
from app.schemas.general_schemas import SuccessResponseSchema

class LoginRequestSchema(BaseModel, EmailValidator):
    email: EmailStr
    password: str

    class Config: 
        extra = "ignore"

class SuccessLoginDataSchema(BaseModel):
    access_token: str
    expiry_time: str
    user: dict

class LoginResponseSchema(SuccessResponseSchema):
    data: SuccessLoginDataSchema