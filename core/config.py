from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Base
    PROJECT_NAME: str = "Event Finder Worker"

    # Logging
    LOG_LEVEL: str = "INFO"

    # Email (Mailgun)
    MAILGUN_API_KEY: str = ""
    MAILGUN_DOMAIN: str = ""

    # Upstash Redis
    UPSTASH_REDIS_REST_URL: str = ""
    UPSTASH_REDIS_REST_TOKEN: str = ""

    class Config:
        case_sensitive = True
        env_file = ".env"
        extra = "allow"


settings = Settings()
