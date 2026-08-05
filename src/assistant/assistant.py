from conversation.manager import ConversationManager

from ai.prompts import system_prompt

from agent.planner import Planner
from agent.dispatcher import Dispatcher
from agent.router import Router

from audio.speaker import Speaker


class ManasAssistant:

    def __init__(self):

        self.memory = ConversationManager()

        self.memory.add(
            "system",
            system_prompt()
        )

        self.planner = Planner()
        self.dispatcher = Dispatcher()
        self.router = Router()

        self.speaker = Speaker()

    def ask(self, message: str):

        print("=" * 60)
        print("USER:", message)

        self.memory.add(
            "user",
            message
        )

        print("Calling Planner...")

        plan = self.planner.plan(
            self.memory.history()
        )

        print("Plan:", plan)

        result = self.dispatcher.dispatch(plan)

        print("RESULT:", result)

        self.memory.add(
            "assistant",
            str(result)
        )

        route = self.router.route(message)

        print("ROUTE:", route)
        print("=" * 60)

        if isinstance(result, dict):
            response = result.get("response", "")
        else:
            response = str(result)

        if response:
            self.speaker.speak(response)

        return response