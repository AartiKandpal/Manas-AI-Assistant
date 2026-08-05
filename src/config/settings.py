from dataclasses import dataclass


@dataclass
class Settings:

    APP_NAME = "Manas"

    MODEL = "qwen2.5:3b"

    OLLAMA_HOST = "http://localhost:11434"

    DATABASE = "manas.db"

    VERSION = "3.1"

    DEBUG = True