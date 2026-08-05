from memory.database import MemoryDatabase


class MemoryManager:

    def __init__(self):
        self.memory = MemoryDatabase.load()

    def remember(self, key: str, value: str):

        self.memory[key] = value
        MemoryDatabase.save(self.memory)

        return "I'll remember that."

    def recall(self, key: str):

        return self.memory.get(key)

    def forget(self, key: str):

        self.memory.pop(key, None)
        MemoryDatabase.save(self.memory)

        return "Forgotten."

    def all(self):

        return self.memory