import pygame
from enemy import Enemy


class BuzzyBeetle(Enemy):
    def __init__(self, settings, screen, x, y):
        super(BuzzyBeetle, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.buzzy_width, settings.buzzy_height)
        self.pic = pygame.image.load('images/Buzzy_Beetle1.png')
        self.image = pygame.transform.scale(self.pic, (settings.buzzy_width, settings.buzzy_height))
