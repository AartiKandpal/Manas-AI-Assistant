import pygame
import time
import os


class AudioPlayer:
    def __init__(self):
        pygame.mixer.init()

    def play(self, file_path):
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

        pygame.mixer.music.unload()
        os.remove(file_path)