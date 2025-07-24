from xml.dom import NotFoundErr
from openai import AsyncOpenAI
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.course import Course
from app.schemas.course import CourseResponse, CourseCreate, CourseUpdate
from app.config import config
from app.repository.course import CourseRepository

client = AsyncOpenAI(
    api_key=config.openai.api_key,
)


class CourseService:
    @staticmethod
    async def sumbit_courser(
        db: AsyncSession, course: CourseCreate, user_id: int
    ) -> Course:
        new_course = await CourseRepository.create_course(db, course, user_id)
        return new_course

    @staticmethod
    async def generate_summary(db: AsyncSession, course_id: int) -> Course:
        course = await CourseRepository.get_course_by_id(db, course_id)
        if course is None:
            raise NotFoundErr(f"No course with id {course_id}")
        completion = await client.chat.completions.create(
            model="gpt-4o-mini",
            # possiable promt attack
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that summarizes online courses.",
                },
                {
                    "role": "user",
                    "content": f"Summarize this online course: {course.course_description}",
                },
            ],
        )
        summary = completion.choices[0].message.content
        if summary is None or summary == "":
            raise NotFoundErr(f"No summary generated for course with id {course_id}")
        course_update = CourseUpdate(ai_summary=summary, status="completed")
        course = await CourseRepository.update_course(db, course, course_update)

        return course
