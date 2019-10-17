import pygame
from enemy import Enemy


class Koopa_Troopa(Enemy):
    def __init__(self, settings, screen, x, y):
        super(Koopa_Troopa, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.koopa_width, settings.koopa_height)
        self.pic = pygame.image.load('images/Koopa1.png')
        self.image = pygame.transform.scale(self.pic, (settings.koopa_width, settings.koopa_height))

    def update(self):
        self.x += self.settings.koopa_speed * self.x_direction
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
