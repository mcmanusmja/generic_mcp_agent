from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Create settings instance
    settings = Settings()

    print("Hello from generic-mcp-agent!")
    print(f"Settings loaded: {settings}")


if __name__ == "__main__":
    main()
