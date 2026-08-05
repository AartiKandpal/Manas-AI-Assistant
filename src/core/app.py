from assistant.assistant import ManasAssistant
from audio.voice import VoiceAssistant


class ManasApp:

    def __init__(self):

        self.assistant = ManasAssistant()
        self.voice = VoiceAssistant()

    def run(self):

        print("=" * 50)
        print("🤖 Manas AI")
        print("Voice Mode Ready")
        print("=" * 50)

        while True:

            try:

                text = self.voice.listen()

                if not text:
                    continue

                print(f"\nYou : {text}")

                reply = self.assistant.ask(text)

                print(f"\nManas : {reply}")

                self.voice.speak(reply)

            except KeyboardInterrupt:

                print("\nStopping Manas...")

                break

            except Exception as e:

                print(f"\nERROR: {e}")