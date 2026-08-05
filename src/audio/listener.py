import tempfile
import sounddevice as sd
from scipy.io.wavfile import write
from faster_whisper import WhisperModel


class Listener:

    def __init__(self):

        print("Loading Whisper model...")

        self.model = WhisperModel(
            "base",
            device="cpu",
            compute_type="int8"
        )

    def listen(self):

        fs = 16000
        duration = 5

        print("Listening...")

        audio = sd.rec(
            int(duration * fs),
            samplerate=fs,
            channels=1,
            dtype="int16"
        )

        sd.wait()

        with tempfile.NamedTemporaryFile(
            suffix=".wav",
            delete=False
        ) as f:

            write(f.name, fs, audio)

            segments, _ = self.model.transcribe(f.name)

            text = ""

            for segment in segments:
                text += segment.text

        text = text.strip()

        print("You:", text)

        return text