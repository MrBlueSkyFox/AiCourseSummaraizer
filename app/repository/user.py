from typing import Optional, TypeVar
from sqlalchemy import Integer, cast, select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate

T = TypeVar("T")


class UserRepository:
    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate) -> User:
        new_user = User(name=user.name, email=user.email, password=user.password)
        new_user = await UserRepository.save(db, new_user)
        return new_user

    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
        query = select(User).where(cast(User.id, Integer) == user_id)
        result = await db.execute(query)
        user = result.scalar_one_or_none()
        return user

    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
        result = await db.execute(select(User).filter(User.email == email))
        user = result.scalar_one_or_none()
        return user

    @staticmethod
    async def save(db: AsyncSession, obj: T) -> T:
        db.add(obj)
        await db.flush()
        await db.refresh(obj)
        return obj
