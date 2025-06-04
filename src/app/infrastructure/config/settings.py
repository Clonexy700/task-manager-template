from pydantic_settings import BaseSettings


class PostgreSQLSettings(BaseSettings):
    POSTGRES_USER: str = 'postgresql'
    POSTGRES_PASSWORD: str = "1234"
    POSTGRES_DB_NAME: str = 'postgresql'
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/"
            f"{self.POSTGRES_DB_NAME}"
        )


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = PostgreSQLSettings()
