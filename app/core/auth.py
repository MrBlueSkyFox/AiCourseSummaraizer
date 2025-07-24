from xml.dom import NotFoundErr
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.ext.asyncio import AsyncSession
from app.config import config
from app.core.database import get_session
from app.models.user import User
from app.schemas.user import UserResponse
from app.services.user import UserService
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_session)) -> UserResponse:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, config.app.secret_key, algorithms=[config.app.algorithm])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    try:
        user = await UserService.get_user_by_id(db, user_id)
    except NotFoundErr as e:
        raise credentials_exception
    return UserResponse.model_validate(user)