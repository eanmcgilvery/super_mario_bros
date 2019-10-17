import pygame
from pygame.sprite import Sprite


class Goomba(Sprite):
    def __init__(self, settings, screen, x, y):
        super(Goomba, self).__init__()
        self.settings = settings
        self.screen = screen

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.goomba_width, settings.goomba_height)
        self.pic = pygame.image.load('images/Goomba1.png')
        self.image = pygame.transform.scale(self.pic, (settings.goomba_width, settings.goomba_height))

        # Initial movement direction is left
        self.direction = -1

        # Store exact position
        self.x = x
        self.y = y

    def update(self):
        self.rect.x += self.settings.goomba_speed * self.direction

    def blitme(self):
        self.screen.blit(self.image, self.rect)
