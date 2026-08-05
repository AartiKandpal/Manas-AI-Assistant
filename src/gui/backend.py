from assistant.assistant import ManasAssistant


class Backend:

    def __init__(self):
        print("Backend initialized")
        self.assistant = ManasAssistant()

    def ask(self, text):

        print("=" * 50)
        print("Backend.ask()")
        print("User:", text)

        reply = self.assistant.ask(text)

        print("Assistant Reply:", reply)
        print("=" * 50)

        # If assistant returns a dictionary
        if isinstance(reply, dict):
            return reply.get("response", "")

        # If assistant returns a Plan object
        if hasattr(reply, "response"):
            return reply.response

        # Otherwise return whatever it is
        return str(reply)