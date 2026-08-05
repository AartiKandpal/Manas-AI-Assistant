from audio.recorder import AudioRecorder
from audio.stt import SpeechToText
from audio.tts import TextToSpeech
from audio.player import AudioPlayer
from audio.wake_word import WakeWordDetector


class VoiceAssistant:

    def __init__(self):

        self.wake = WakeWordDetector()

        self.recorder = AudioRecorder()
        self.stt = SpeechToText()
        self.tts = TextToSpeech()
        self.player = AudioPlayer()

    def listen(self):

        # Wait until wake word is detected
        self.wake.wait()

        print("🎤 Speak now...")

        audio = self.recorder.record()

        if audio is None:
            return None

        text = self.stt.transcribe(audio)

        return text.strip()

    def speak(self, text):

        audio_file = self.tts.generate(text)

        self.player.play(audio_file)