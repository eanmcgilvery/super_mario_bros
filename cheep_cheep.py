import pygame
from enemy import Enemy


class CheepCheep(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(CheepCheep, self).__init__(settings, screen, x, y, etype)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.cheep_width, settings.cheep_height)
        self.pic = pygame.image.load('images/Cheep_cheep1.png')
        self.image = pygame.transform.scale(self.pic, (settings.cheep_width, settings.cheep_height))
