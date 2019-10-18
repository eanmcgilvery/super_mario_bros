import pygame
from enemy import Enemy


class Spiny(Enemy):
    def __init__(self, settings, screen, x, y):
        super(Spiny, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.spiny_width, settings.spiny_height)
        self.pic = pygame.image.load('images/Spiny1.png')
        self.image = pygame.transform.scale(self.pic, (settings.spiny_width, settings.spiny_height))
