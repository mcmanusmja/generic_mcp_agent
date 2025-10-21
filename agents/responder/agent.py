from core.base_agent import MCPAgent
from schemas.context import TaskContext


class ResponderAgent(MCPAgent):
    def __init__(self):
        super().__init__(name="responder")

    def run(self, context: TaskContext) -> dict:
        response_text = f"Received your request to: {context.objective}"
        return {
            "task_id": context.task_id,
            "response": response_text
        }
