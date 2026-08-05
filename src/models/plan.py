from pydantic import BaseModel, Field

from models.tool_call import ToolCall


class Plan(BaseModel):
    """
    Final planning object returned by the LLM.

    - tools: list of tool calls to execute.
    - response: text response from the model.
    """

    tools: list[ToolCall] = Field(default_factory=list)

    response: str = ""

    @property
    def has_tools(self) -> bool:
        return len(self.tools) > 0

    @property
    def first_tool(self):
        if not self.tools:
            return None
        return self.tools[0]