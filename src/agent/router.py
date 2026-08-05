import re


class Router:

    def route(self, message: str):

        text = message.lower()

        if re.search(r"\b(open|launch|start)\b", text):
            return "tool"

        if re.search(r"\b(create|delete|rename|move|copy)\b", text):
            return "tool"

        if re.search(r"\b(search|google|youtube)\b", text):
            return "tool"

        if re.search(r"\b(remember|recall)\b", text):
            return "tool"

        return "llm"