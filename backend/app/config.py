from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Internship Roadmap Generator"
    VERSION: str = "1.0.0"

    DATABASE_URL: str = "sqlite:///./ai_roadmap.db"

    SECRET_KEY: str = "ezitech-secret-key"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    class Config:
        env_file = ".env"


settings = Settings()