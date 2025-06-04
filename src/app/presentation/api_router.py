from fastapi import APIRouter
from src.app.presentation.v1.routers import shift_tasks

api_router = APIRouter()
api_router.include_router(shift_tasks.router, prefix="/api/v1", tags=["Shift Tasks"])
