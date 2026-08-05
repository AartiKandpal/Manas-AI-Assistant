from memory.manager import MemoryManager


class MemoryTools:

    manager = MemoryManager()

    @staticmethod
    def remember(key: str, value: str):
        return MemoryTools.manager.remember(key, value)

    @staticmethod
    def recall(key: str):

        value = MemoryTools.manager.recall(key)

        if value is None:
            return "I don't know."

        return value

    @staticmethod
    def forget(key: str):
        return MemoryTools.manager.forget(key)

    @staticmethod
    def show_memory():
        return str(MemoryTools.manager.all())