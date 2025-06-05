from pydantic_settings import BaseSettings


class PostgreSQLSettings(BaseSettings):
    """
    f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
    f"@{self.DB_HOST}:{self.DB_PORT}/"
    f"{self.POSTGRES_DB_NAME}"
    """
    POSTGRES_USER: str = 'postgresql'
    POSTGRES_PASSWORD: str = "1234"
    POSTGRES_DB_NAME: str = 'postgresql'
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return (
            "sqlite:///./test.db")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = PostgreSQLSettings()
