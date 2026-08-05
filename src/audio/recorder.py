import tempfile
import wave

import sounddevice as sd
import numpy as np


class AudioRecorder:

    def __init__(self):
        self.sample_rate = 16000
        self.channels = 1
        self.duration = 5  # seconds

    def record(self):

        print("🎤 Speak now...")

        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=self.channels,
            dtype="int16",
        )

        sd.wait()

        path = tempfile.mktemp(suffix=".wav")

        with wave.open(path, "wb") as wf:
            wf.setnchannels(self.channels)
            wf.setsampwidth(2)
            wf.setframerate(self.sample_rate)
            wf.writeframes(audio.tobytes())

        return path