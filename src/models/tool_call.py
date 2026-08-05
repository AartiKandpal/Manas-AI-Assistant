from typing import Any

from pydantic import BaseModel, Field


class ToolCall(BaseModel):
    """
    Represents a single tool invocation requested by the LLM.
    """

    tool: str

    arguments: dict[str, Any] = Field(default_factory=dict)

    @property
    def name(self) -> str:
        return self.tool