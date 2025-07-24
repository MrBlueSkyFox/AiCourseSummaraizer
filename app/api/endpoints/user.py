from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.auth import get_current_user
from app.core.database import get_session
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter()


@router.post("/users", response_model=UserResponse)
async def create_new_user(user: UserCreate, db: AsyncSession = Depends(get_session)):
    return await UserService.create_user(db, user)


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user_details(
    user_id: int,
    db: AsyncSession = Depends(get_session),
    _: UserResponse = Depends(get_current_user),
):
    user = await UserService.get_user_by_id(db, user_id)
    return user
