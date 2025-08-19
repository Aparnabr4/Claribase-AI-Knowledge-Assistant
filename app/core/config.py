from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = "/Users/aparna/PycharmProjects/claribase/app/.env"

class Settings(BaseSettings):
    PROJECT_NAME: str = "ClariBase"
    PROJECT_VERSION: str = "0.1.0"

    GROQ_API_KEY: str | None = None

    EMAIL_HOST: str | None = None
    EMAIL_PORT: int | None = None
    EMAIL_USERNAME: str | None = None
    EMAIL_PASSWORD: str | None = None
    EMAIL_FROM: str | None = None

    model_config = SettingsConfigDict(
        env_file=BASE_DIR,  # now looking inside app/
        extra="ignore"
    )


settings = Settings()

class Health(BaseModel):
    status: str = "ok"
    version: str = settings.PROJECT_VERSION
    openai: bool = bool(settings.GROQ_API_KEY)
    email_ready: bool = all([
        settings.EMAIL_HOST, settings.EMAIL_PORT, settings.EMAIL_USERNAME,
        settings.EMAIL_PASSWORD, settings.EMAIL_FROM
    ])