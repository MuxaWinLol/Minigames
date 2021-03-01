import pygame


def play_music():
    pygame.mixer.music.load(r'data\sound_0.mp3')
    for i in range(6, 0, -1):
        pygame.mixer.music.queue(r'data\sound_{}.mp3'.format(i))
    pygame.mixer.music.play()
