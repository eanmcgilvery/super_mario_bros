import pygame
from enemy import Enemy


class Lakitu(Enemy):
    def __init__(self, settings, screen, x, y):
        super(Lakitu, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.lakitu_width, settings.lakitu_height)
        self.pic = pygame.image.load('images/Lakitu1.png')
        self.image = pygame.transform.scale(self.pic, (settings.lakitu_width, settings.lakitu_height))
