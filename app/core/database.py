from asyncio import shield
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from app.config import config
from sqlalchemy.exc import DBAPIError

DATABASE_URL = f"postgresql+asyncpg://{config.postgres.user}:{config.postgres.password}@{config.postgres.host}:{config.postgres.port}/{config.postgres.db}"

def get_async_session():

    async_engine = create_async_engine(
        DATABASE_URL,
        pool_pre_ping=True,
        connect_args={"server_settings": {"jit": "off"}},
    )

    AsyncSessionLocal = async_sessionmaker(bind=async_engine, expire_on_commit=False, class_=AsyncSession)
    return AsyncSessionLocal()


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session: AsyncSession = get_async_session()
    try:
        yield session
        await session.commit()
    except DBAPIError as e:
        await session.rollback()
        raise e
    except Exception:
        await session.rollback()
        raise
    finally:
        if session:
            await shield(session.close())
