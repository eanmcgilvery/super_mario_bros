import pygame
import sys

from settings import Settings as s

class Level1_1:
    def __init__(self):

        self.setup_backgroud()


    def setup_background(self):
        """Setting up background"""

        self.background = pyame.image.load('image/level1_1.png')
        self.back_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.back_rect.width*s.background_multipler), int(self.back_rect.height*s.background_multipler)))
        self.back_rect = self.background.get_rect()

        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pygame.Suface((width, height)).convert()
        self.level_rect = self.level.get_rect()

        screen = pygame.display.set_mode(s.screen_size)
        screen_rect = screen.get_rect()

        self.viewport = screen_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game.info['camera start x']


