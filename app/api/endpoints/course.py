from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_session
from app.core.auth import get_current_user
from app.schemas.course import CourseCreate, CourseResponse
from app.schemas.user import UserResponse
from app.services.course import CourseService

router = APIRouter()


@router.post("/courses", response_model=CourseResponse)
async def submit_course_description(
    course: CourseCreate,
    db: AsyncSession = Depends(get_session),
    user: UserResponse = Depends(get_current_user),
):
    return await CourseService.sumbit_courser(db, course, user.id)


@router.post("/generate_summary/{course_id}")
async def generate_summary(
    course_id: int,
    db: AsyncSession = Depends(get_session),
    _: UserResponse = Depends(get_current_user),
):
    return await CourseService.generate_summary(db, course_id)
