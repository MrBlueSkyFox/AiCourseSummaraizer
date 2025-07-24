from typing import Optional, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.course import Course
from app.schemas.course import CourseCreate, CourseResponse, CourseUpdate

T = TypeVar("T")


class CourseRepository:
    @staticmethod
    async def create_course(db: AsyncSession, course: CourseCreate, user_id: int) -> Course:
        new_course = Course(
            course_title=course.course_title,
            course_description=course.course_description,
            status="pending",
            user_id=user_id,
            ai_summary="",
        )
        new_course = await CourseRepository.save(db, new_course)
        return new_course

    @staticmethod
    async def get_course_by_id(db: AsyncSession, course_id: int) -> Optional[Course]:
        result = await db.execute(select(Course).filter(Course.id == course_id))
        course = result.scalar_one_or_none()
        return course

    @staticmethod
    async def update_course(
        db: AsyncSession, course: Course, course_update: CourseUpdate
    ) -> Course:
        course.ai_summary = course_update.ai_summary
        course.status = course_update.status
        await db.flush()
        await db.refresh(course)
        return course

    @staticmethod
    async def save(db: AsyncSession, obj: T) -> T:
        db.add(obj)
        await db.flush()
        await db.refresh(obj)
        return obj
