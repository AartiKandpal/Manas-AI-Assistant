from ai.llm import LocalLLM
from models.plan import Plan


class Planner:

    def __init__(self):

        print("=" * 60)
        print("Planner initializing...")
        self.llm = LocalLLM()
        print("LLM initialized successfully.")
        print("=" * 60)

    def plan(self, messages) -> Plan:

        print("=" * 60)
        print("Entered Planner.plan()")
        print(f"Messages received: {len(messages)}")
        print("Calling llm.chat()...")
        print("=" * 60)

        try:
            result = self.llm.chat(messages)

            print("=" * 60)
            print("Returned from llm.chat()")
            print("Raw Result:")
            print(result)
            print("=" * 60)

        except Exception as e:

            print("=" * 60)
            print("ERROR inside llm.chat()")
            print(type(e).__name__)
            print(e)
            print("=" * 60)

            return Plan(
                tools=[],
                response=f"LLM Error: {e}"
            )

        if isinstance(result, Plan):

            print("Result already a Plan object.")
            return result

        if not isinstance(result, dict):

            print("Result is not a dictionary.")

            return Plan(
                tools=[],
                response="Sorry, I couldn't understand the request."
            )

        result.setdefault("tools", [])
        result.setdefault("response", "")

        try:

            plan = Plan(**result)

            print("=" * 60)
            print("Plan created successfully.")
            print(plan)
            print("=" * 60)

            return plan

        except Exception as e:

            print("=" * 60)
            print("Planner Error while creating Plan")
            print(type(e).__name__)
            print(e)
            print("Result was:")
            print(result)
            print("=" * 60)

            return Plan(
                tools=[],
                response="Sorry, something went wrong while planning."
            )