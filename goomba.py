import pygame
from enemy import Enemy


class Goomba(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(Goomba, self).__init__(settings, screen, x, y, etype)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.goomba_width, settings.goomba_height)
        self.pic = pygame.image.load('images/Goomba1a1.png')
        self.image = pygame.transform.scale(self.pic, (settings.goomba_width, settings.goomba_height))

    def update_pos(self):
        self.x += self.settings.goomba_speed * self.x_direction
        self.rect.x = self.x

    def update_image(self):
        if self.frame is 1:
            self.frame = 2
            self.pic = pygame.image.load('images/Goomba1a2.png')
        elif self.frame is 2:
            self.frame = 1
            self.pic = pygame.image.load('images/Goomba1a1.png')
        self.image = pygame.transform.scale(self.pic, (self.settings.goomba_width, self.settings.goomba_height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
