from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
import sqlalchemy.sql.functions
from app.models.base import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    course_title = Column(String(255), nullable=False)
    course_description = Column(Text, nullable=False)
    ai_summary = Column(Text)
    status = Column(String(50), default="pending")
    created_at = Column(TIMESTAMP, server_default=sqlalchemy.sql.functions.now())
