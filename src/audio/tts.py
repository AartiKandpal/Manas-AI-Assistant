import asyncio
import edge_tts
import tempfile
import os


class TextToSpeech:
    def __init__(self, voice="en-US-AriaNeural"):
        self.voice = voice

    async def _generate(self, text):
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
        temp_file.close()

        communicate = edge_tts.Communicate(text=text, voice=self.voice)
        await communicate.save(temp_file.name)

        return temp_file.name

    def generate(self, text):
        return asyncio.run(self._generate(text))