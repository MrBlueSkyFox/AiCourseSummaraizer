from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import config
from app.core.enums import Environment
from app.api.router import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(api_router, prefix="")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        host=config.app.host,
        port=config.app.port,
        app="app.main:app" if config.app.environment == Environment.LOCAL else app,
        reload=config.app.environment == Environment.LOCAL,
        workers=(
            1 if config.app.environment == Environment.LOCAL else config.app.workers
        ),
    )
