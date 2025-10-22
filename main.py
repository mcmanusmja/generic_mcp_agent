from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

from agents.responder.agent import ResponderAgent
from schemas.message import MCPMessage


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    ollama_api_key: str = Field(alias="OLLAMA_API_KEY")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


def main():
    # Load environment variables from .env file
    load_dotenv()

    # Create settings instance
    settings = Settings()

    print("Hello from generic-mcp-agent!")
    print(f"Settings loaded: {settings}")

    message = MCPMessage(
        sender="planner",
        receiver="responder",
        type="task_request",
        payload={
            "task_id": "T-001",
            "objective": "Generare a summary of benefits",
            "format": "markdown",
            "language": "en"
        }
    )

    agent = ResponderAgent()
    response = agent(message)
    print(response.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
