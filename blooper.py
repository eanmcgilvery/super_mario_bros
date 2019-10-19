import pygame
from enemy import Enemy


class Blooper(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(Blooper, self).__init__(settings, screen, x, y, etype)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.blooper_width, settings.bloopera1_height)
        self.pic = pygame.image.load('images/Bloopera1.png')
        self.image = pygame.transform.scale(self.pic, (settings.blooper_width, settings.bloopera1_height))

    def update_pos(self):
        self.x += self.settings.blooper_speed * self.x_direction
        self.rect.x = self.x

    def update_image(self):
        # Animation tied into movement
        if self.frame is 1:
            self.rect = pygame.Rect(self.x, self.y, self.settings.blooper_width, self.settings.bloopera2_height)
            self.pic = pygame.image.load('images/Bloopera2.png')
            self.image = pygame.transform.scale(self.pic, (self.settings.blooper_width, self.settings.bloopera2_height))
            self.frame = 2
        elif self.frame is 2:
            self.rect = pygame.Rect(self.x, self.y, self.settings.blooper_width, self.settings.bloopera1_height)
            self.pic = pygame.image.load('images/Bloopera1.png')
            self.image = pygame.transform.scale(self.pic, (self.settings.blooper_width, self.settings.bloopera1_height))
            self.frame = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
