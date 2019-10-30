import pygame
from object import Object


class Bush(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Bush, self).__init__(settings, screen, x, y, otype)

        # Rect, image, and initial position set up
        if self.otype is 1:
            self.pic = pygame.image.load('images/bush1.png')
            self.rect = pygame.Rect(x, y, settings.small_bush_width, settings.small_bush_height)
            self.image = pygame.transform.scale(self.pic, (settings.small_bush_width, settings.small_bush_height))
        elif self.otype is 2:
            self.pic = pygame.image.load('images/bush2.png')
            self.rect = pygame.Rect(x, y, settings.medium_bush_width, settings.medium_bush_height)
            self.image = pygame.transform.scale(self.pic, (settings.medium_bush_width, settings.medium_bush_height))
        elif self.otype is 3:
            self.pic = pygame.image.load('images/bush3.png')
            self.rect = pygame.Rect(x, y, settings.large_bush_width, settings.large_bush_height)
            self.image = pygame.transform.scale(self.pic, (settings.large_bush_width, settings.large_bush_height))

    def update_image(self):
        self.image = self.image

    def blitme(self):
        self.screen.blit(self.image, self.rect)
