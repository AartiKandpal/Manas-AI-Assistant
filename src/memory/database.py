import json
from pathlib import Path

MEMORY_FILE = Path("memory/memory.json")


class MemoryDatabase:

    @staticmethod
    def load():

        if not MEMORY_FILE.exists():
            return {}

        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def save(data):

        with open(MEMORY_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)