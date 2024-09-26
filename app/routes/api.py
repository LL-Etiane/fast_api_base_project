from fastapi import APIRouter
from app.controllers.auth_controller import router as auth_router

router = APIRouter(prefix="/api/v1")

router.include_router(auth_router)
