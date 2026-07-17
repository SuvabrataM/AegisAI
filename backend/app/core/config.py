from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    PROJECT_NAME: str = "Aegis AI"

    PROJECT_VERSION: str = "1.0.0"

    PROJECT_DESCRIPTION: str = (
        "An AI-powered platform that helps engineering teams "
        "search operational knowledge, investigate incidents, "
        "and interact with enterprise documentation using LLMs."
    )

    PROJECT_AUTHOR: str = "Suvabrata Mukherjee"

    PROJECT_EMAIL: str = "suva.aec07@example.com"

    API_V1_PREFIX: str = "/api/v1"

    DEBUG: bool = True

    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()