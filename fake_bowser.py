import pygame
from enemy import Enemy


class FakeBowser(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(FakeBowser, self).__init__(settings, screen, x, y, etype)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.fake_bowser_width, settings.fake_bowser_height)
        self.pic = pygame.image.load('images/Fake_Bowser1.png')
        self.image = pygame.transform.scale(self.pic, (settings.fake_bowser_width, settings.fake_bowser_height))
