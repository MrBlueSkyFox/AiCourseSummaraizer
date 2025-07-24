from pydantic import BaseModel

class CourseBase(BaseModel):
    course_title: str
    course_description: str

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    ai_summary: str
    status: str

class CourseUpdate(BaseModel):
    ai_summary: str
    status: str