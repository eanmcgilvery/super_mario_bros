import pygame
from enemy import Enemy


class Goomba(Enemy):
    def __init__(self, settings, screen, x, y):
        super(Goomba, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.goomba_width, settings.goomba_height)
        self.pic = pygame.image.load('images/Goomba1.png')
        self.image = pygame.transform.scale(self.pic, (settings.goomba_width, settings.goomba_height))

    def update(self):
        self.x += self.settings.goomba_speed * self.x_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
