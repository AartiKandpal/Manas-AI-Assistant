from models.plan import Plan
from tools.manager import ToolManager


class Dispatcher:
    def __init__(self):
        self.tool_manager = ToolManager()

    def dispatch(self, plan: Plan):

        if not isinstance(plan, Plan):
            raise TypeError(
                f"Expected Plan, got {type(plan)}"
            )

        if not plan.tools:
            return plan.response

        results = []

        for tool_call in plan.tools:

            result = self.tool_manager.execute(tool_call)

            results.append(str(result))

        if plan.response.strip():
            results.append(plan.response)

        return "\n".join(results)