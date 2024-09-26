from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.auth_schemas import LoginRequestSchema, LoginResponseSchema
from app.dependencies import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=LoginResponseSchema)
async def login(data: LoginRequestSchema, db=Depends(get_db)):
    return {"message": "Login route"}