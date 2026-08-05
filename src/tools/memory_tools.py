from memory.memory_store import MemoryStore


class MemoryTools:

    store = MemoryStore()

    @staticmethod
    def remember(key: str, value: str):
        return MemoryTools.store.remember(key, value)

    @staticmethod
    def recall(key: str):
        value = MemoryTools.store.recall(key)

        if value is None:
            return f"I don't know '{key}'."

        return value

    @staticmethod
    def forget(key: str):
        return MemoryTools.store.forget(key)

    @staticmethod
    def show_memory():
        memory = MemoryTools.store.show()

        if not memory:
            return "Memory is empty."

        return "\n".join(
            f"{k}: {v}"
            for k, v in memory.items()
        )