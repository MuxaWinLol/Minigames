import pygame


def play_music():
    for i in range(7):
        pygame.mixer.music.load(r'data\sound_{}.mp3'.format(i))
    pygame.mixer.music.play()