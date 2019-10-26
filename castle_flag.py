import pygame
from object import Object

class CastleFlag(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(CastleFlag, self).__init__(settings, screen, x, y, otype)

        # Rect, image, and initial position set up
        self.pic = pygame.image.load('images/castle_flag.png')
        self.rect = pygame.Rect(x, y, settings.castle_flag_width, settings.castle_flag_height)
        self.image = pygame.transform.scale(self.pic, (settings.castle_flag_width, settings.castle_flag_height))

    def update_image(self):
        self.image = self.image




    def blitme(self):
        self.screen.blit(self.image, self.rect)