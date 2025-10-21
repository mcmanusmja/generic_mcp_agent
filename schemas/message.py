from pydantic import BaseModel, Field
from typing import Literal, Optional
from datetime import datetime, timezone


class MCPMessage(BaseModel):
    sender: str
    receiver: str
    type: Literal["task_request", "result", "error"]
    payload: dict
    timestamp: Optional[datetime] = Field(
        default_factory=datetime.now(timezone.utc))
