from abc import ABC, abstractmethod
from datetime import datetime, timezone
from pydantic import BaseModel, ValidationError
from schemas.message import MCPMessage
from schemas.context import TaskContext


class MCPAgent(ABC):
    name: str  # e.g. "responder", "planner"

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def __call__(self, message: MCPMessage) -> MCPMessage:
        return self.handle_message(message)

    def handle_message(self, message: MCPMessage) -> MCPMessage:
        try:
            self.validate_recipient(message)
            context = self.validate_context(message.payload)
            result = self.run(context)
            return self.create_response(message, result)
        except ValidationError as e:
            return self.create_error_response(message, "Validation error", str(e))

        except Exception as e:
            return self.create_error_response(message, "AgentExecutionError", str(e))

    def validate_recipient(self, message: MCPMessage) -> None:
        if message.receiver != self.name:
            raise ValueError(
                f"Agent {self.name} received a message not meant for it!")

    def validate_context(self, payload: dict) -> TaskContext:
        return TaskContext.model_validate(payload)

    @abstractmethod
    def run(self, context: TaskContext) -> dict:
        """Chile agents must override this method with actual logic."""
        pass

    def create_response(self, request: MCPMessage, result: dict) -> MCPMessage:
        return MCPMessage(
            sender=self.name,
            receiver=request.sender,
            type="result",
            payload=result,
            timestamp=datetime.now(timezone.utc)

        )

    def create_error_response(self, request: MCPMessage, error_type: str, detail: str) -> MCPMessage:
        return MCPMessage(
            sender=self.name,
            receiver=request.sender,
            type="error",
            payload={
                "error_type": error_type,
                "detail": detail,

            },
            timestamp=datetime.now(timezone.utc)

        )
