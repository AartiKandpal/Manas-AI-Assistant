import torch
from silero_vad import (
    load_silero_vad,
    get_speech_timestamps,
)


class VoiceActivityDetector:

    def __init__(self, sample_rate: int = 16000):

        self.sample_rate = sample_rate
        self.model = load_silero_vad()

    def has_speech(self, audio) -> bool:
        """
        Returns True if speech is detected.
        """

        if audio is None:
            return False

        if not isinstance(audio, torch.Tensor):
            audio = torch.tensor(audio, dtype=torch.float32)

        speech = get_speech_timestamps(
            audio,
            self.model,
            sampling_rate=self.sample_rate,
        )

        return len(speech) > 0

    def speech_segments(self, audio):
        """
        Returns all detected speech segments.
        """

        if not isinstance(audio, torch.Tensor):
            audio = torch.tensor(audio, dtype=torch.float32)

        return get_speech_timestamps(
            audio,
            self.model,
            sampling_rate=self.sample_rate,
        )