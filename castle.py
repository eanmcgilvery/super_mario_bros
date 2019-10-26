import pygame
from object import Object

class Castle(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Castle, self).__init__(settings, screen, x, y, otype)

        # Rect, image, and initial position set up
        self.pic = pygame.image.load('images/small_castle.png')
        self.rect = pygame.Rect(x, y, settings.small_castle_width, settings.small_castle_height)
        self.image = pygame.transform.scale(self.pic, (settings.small_castle_width, settings.small_castle_height))

    def update_image(self):
        self.image = self.image

    def update_pos(self):
        self.x -= 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)