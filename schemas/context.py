from pydantic import BaseModel, ConfigDict, Field
from typing import Optional, Literal
from datetime import datetime, timezone


class TaskContext(BaseModel):
    model_config = ConfigDict(strict=True, extra="forbid")
    task_id: str
    objective: str
    format: Optional[Literal["markdown", "json", "html"]] = "markdown"
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))
    language: Optional[str] = "en"
