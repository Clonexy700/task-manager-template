from pydantic_settings import BaseSettings


class PostgreSQLSettings(BaseSettings):
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB_NAME: str
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.DB_PORT}:{self.DB_PORT}/"
            f"{self.POSTGRES_DB_NAME}"
        )


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"