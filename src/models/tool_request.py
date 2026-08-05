from pydantic import BaseModel, Field
from typing import Optional


class ToolRequest(BaseModel):
    tool: Optional[str] = None
    arguments: dict = Field(default_factory=dict)
    response: Optional[str] = None