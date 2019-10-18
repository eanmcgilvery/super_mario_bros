import pygame
from enemy import Enemy


class Blooper(Enemy):
    def __init__(self, settings, screen, x, y):
        super(Blooper, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.blooper_width, settings.blooper_height)
        self.pic = pygame.image.load('images/Blooper1.png')
        self.image = pygame.transform.scale(self.pic, (settings.blooper_width, settings.blooper_height))
