from faster_whisper import WhisperModel
from audio.recorder import AudioRecorder
from rapidfuzz import fuzz

class WakeWordDetector:

    def __init__(self):

        print("Loading Wake Word Detector...")

        self.recorder = AudioRecorder()

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8",
        )

        self.wake_words = [
            "manas",
            "hey manas",
            "hello manas",
        ]

        print("Wake Word Ready.")

    def wait(self):

        while True:

            print("🎤 Waiting for 'Hey Manas'...")

            audio = self.recorder.record()

            if audio is None:
                continue

            segments, _ = self.model.transcribe(audio)

            text = ""

            for segment in segments:
                text += segment.text

            text = text.lower().strip()

            print("Heard:", text)

            for word in self.wake_words:

                score = fuzz.partial_ratio(word.lower(), text.lower())

                print(f"{word} -> {score}")

                if score >= 50:
                    print("✅ Wake word detected")
                    return
           