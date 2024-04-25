from scripts import settings
import pygame



def play_ambient_song():
    pygame.mixer.music.load('sounds/ambient/24b0d8ed4ae4cb2.mp3')
    pygame.mixer.music.play(loops=-1)
    pygame.mixer.music.set_volume(settings.volume)