import json
from core.base_agent import MCPAgent
from schemas.context import TaskContext


class ResponderAgent(MCPAgent):
    def __init__(self):
        super().__init__(name="responder")

    def run(self, context: TaskContext) -> dict:
        message = self.format_response(context)
        return {
            "task_id": context.task_id,
            "response": message,
            "format": context.format,
            "language": "en",
        }

    def format_response(self, context: TaskContext) -> str:
        match context.format:
            case "markdown":
                return f"**Task Received** {context.objective}"
            case "html":
                return f"<strong>Task Received</strong> {context.objective}"
            case "json":
                return json.dumps({"task": context.objective})
            case default:
                return f"Task Received: {context.objective}"
