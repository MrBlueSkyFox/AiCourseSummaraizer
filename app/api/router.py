from fastapi import APIRouter
from app.api.endpoints import user, course, auth

api_router = APIRouter()

api_router.include_router(user.router, tags=["users"])
api_router.include_router(course.router, tags=["courses"])
api_router.include_router(auth.router, tags=["auth"])
