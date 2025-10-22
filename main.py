from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

from agents.responder.agent import ResponderAgent
from agents.responder.agent import ResponderAgentRunnable
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
            "task_id": "T-20251021-001",
            "objective": "Draft an introductory paragraph on the meaning of life.",
            "format": "json",
            "language": "en"
        }
    )

    agent = ResponderAgent()
    response = agent(message)
    print(response.model_dump_json(indent=2))

    runnable = ResponderAgentRunnable()

    test_input = {
        "sender": "planner",
        "receiver": "responder",
        "type": "task_request",
        "payload": {
            "task_id": "T-808",
            "objective": "Summarize the objective",
            "format": "html"

        }
    }

    output = runnable.invoke(test_input)
    print(f"output from runnable is: {output}")


if __name__ == "__main__":
    main()
