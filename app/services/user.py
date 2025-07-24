from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate
from app.repository.user import UserRepository


class UserService:

    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate) -> User:
        hashed_password = get_password_hash(user.password)
        user.password = hashed_password
        new_user = await UserRepository.create_user(db, user)
        return new_user

    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int) -> User:
        user_id = int(user_id)
        user = await UserRepository.get_by_id(db, user_id)
        if user is None:
            raise HTTPException(status_code=404, detail=f"No user with id {user_id}")
        return user

    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str) -> User:
        user = await UserRepository.get_user_by_email(db, email)
        if user is None:
            raise HTTPException(status_code=404, detail=f"No user with email {email}")
        return user
    
    @staticmethod
    async def authenticate_user(db: AsyncSession, email: str, password: str) -> User:
        user = await UserRepository.get_user_by_email(db, email)
        if user is None or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Incorrect email or password")
        return user