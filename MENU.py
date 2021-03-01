import sys

import pygame
from pygame.locals import *

from py2048 import DveTysyachiSorokVosyem
from tetris import Tetris


class Menu:
    def __init__(self):
        pygame.init()
        self.cl = pygame.time.Clock()
        self.font = pygame.font.SysFont("Comic Sans MS", 20)
        self.button_1 = pygame.Rect(50, 100, 200, 50)
        self.button_2 = pygame.Rect(50, 200, 200, 50)
        self.draw()

        self.screen = pygame.display.set_mode((500, 500), 0, 32)
        self.playing = False

    def draw(self):
        pygame.display.set_caption("Main Menu")
        programicon = pygame.image.load('icons/menu.png')
        pygame.display.set_icon(programicon)
        self.screen = pygame.display.set_mode((500, 500), 0, 32)
        self.screen.fill((0, 0, 0))
        self.draw_text('main menu', self.font, (255, 255, 255), self.screen, 20, 20)
        pygame.draw.rect(self.screen, (255, 0, 0), self.button_1)
        pygame.draw.rect(self.screen, (255, 0, 0), self.button_2)

    @staticmethod
    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu(self):
        click = False
        while True:

            if not self.playing:
                self.draw()
            else:
                with open("game_end.txt", "r+") as fil:
                    if fil.read():
                        self.playing = False

            mx, my = pygame.mouse.get_pos()
            if click:
                if self.button_1.collidepoint((mx, my)):

                    g = DveTysyachiSorokVosyem(self.screen)
                    g.play()
                    self.playing = True
                elif self.button_2.collidepoint((mx, my)):
                    g = Tetris(self.screen)
                    g.cycle()
                    self.playing = True

            click = False
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True

            pygame.display.update()
            self.cl.tick(60)


if __name__ == '__main__':
    m = Menu()
    m.main_menu()
