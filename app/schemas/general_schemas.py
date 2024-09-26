from fastapi import status as status_codes
from pydantic import BaseModel
from typing import Optional, Any

class SuccessResponseSchema(BaseModel):
    status: bool = True
    status_code: int = status_codes.HTTP_200_OK
    message: str = "Request was successful"
    data: Optional[dict] = None

class ErrorResponseSchema(BaseModel):
    status: bool = False
    status_code: int = status_codes.HTTP_400_BAD_REQUEST
    message: str = "An error occurred"
    errors: Optional[Any] 
    
class ErrorDetail(BaseModel):
    field: Optional[str]
    detail: str

