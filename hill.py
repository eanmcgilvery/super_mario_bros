import pygame
from object import Object

class Hill(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Hill, self).__init__(settings, screen, x, y, otype)

        # Rect, image, and initial position set up
        if self.otype is 1:
            self.pic = pygame.image.load('images/hill1.png')
            self.rect = pygame.Rect(x, y, settings.small_hill_width, settings.small_hill_height)
            self.image = pygame.transform.scale(self.pic, (settings.small_hill_width, settings.small_hill_height))
        elif self.otype is 2:
            self.pic = pygame.image.load('images/hill2.png')
            self.rect = pygame.Rect(x, y, settings.large_hill_width, settings.large_hill_height)
            self.image = pygame.transform.scale(self.pic, (settings.large_hill_width, settings.large_hill_height))



    def blitme(self):
        self.screen.blit(self.image, self.rect)