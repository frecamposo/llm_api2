from fastapi import APIRouter
from app.resources.example import router as resources_router

router = APIRouter()
router.include_router(resources_router, prefix="/example", tags=["example"])