import pygame
from enemy import Enemy


class HammerBro(Enemy):
    def __init__(self, settings, screen, x, y):
        super(HammerBro, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.hammer_bro_width, settings.hammer_bro_height)
        self.pic = pygame.image.load('images/Hammer_Bro1.png')
        self.image = pygame.transform.scale(self.pic, (settings.hammer_bro_width, settings.hammer_bro_height))
