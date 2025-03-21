from fastapi import APIRouter
from src.controllers.course_controller import router as courses_router
from src.controllers.health_check import router as health_router

router = APIRouter()

# Include Health check endpoint
router.include_router(health_router, tags=["health"])

# Include Courses router
router.include_router(courses_router, prefix="/courses", tags=["courses"])