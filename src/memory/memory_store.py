import json
from pathlib import Path


class MemoryStore:

    def __init__(self, file_path="memory.json"):
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            self.file_path.write_text("{}")

        self.memory = self.load()

    def load(self):
        try:
            return json.loads(
                self.file_path.read_text(encoding="utf-8")
            )
        except Exception:
            return {}

    def save(self):
        self.file_path.write_text(
            json.dumps(
                self.memory,
                indent=4
            ),
            encoding="utf-8"
        )

    def remember(self, key, value):
        self.memory[key] = value
        self.save()
        return f"Remembered {key}."

    def recall(self, key):
        return self.memory.get(key)

    def forget(self, key):
        if key in self.memory:
            del self.memory[key]
            self.save()
            return f"Forgot {key}."
        return f"{key} not found."

    def show(self):
        return self.memory