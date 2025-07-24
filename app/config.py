from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv
from app.core.enums import Environment

load_dotenv()

class OpenAPiSettings(BaseSettings):
    api_key: str = Field(..., alias="OPENAI_API_KEY")

class PostgresSettings(BaseSettings):
    user: str = Field(..., alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")
    db: str = Field(alias="POSTGRES_DB")
    host: str = Field("db", alias="POSTGRES_HOST")  # Default value "db" if not set
    port: int = Field(5432, alias="POSTGRES_PORT")  # Default value 5432 if not set


class AppSettings(BaseSettings):
    host: str = Field("0.0.0.0", alias="APP_HOST")
    port: int = Field(8111, alias="APP_PORT")
    environment: Environment = Field(default=Environment.DEV, alias='ENVIRONMENT')
    workers: int = Field(default=1, alias='APP_WORKERS')
    secret_key: str = Field(..., alias="SECRET_KEY")
    algorithm: str = Field("HS256", alias="ALGORITHM")


class Config(BaseSettings):
    app: AppSettings = AppSettings() # type: ignore
    postgres: PostgresSettings = Field(default=PostgresSettings()) # type: ignore
    openai: OpenAPiSettings = Field(default=OpenAPiSettings()) # type: ignore

config = Config()
