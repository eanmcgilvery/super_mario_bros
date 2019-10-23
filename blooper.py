import pygame
from enemy import Enemy


class Blooper(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(Blooper, self).__init__(settings, screen, x, y, etype)

        # Rect, image, and initial position set up
        self.width = settings.blooper_width
        self.height = settings.bloopera1_height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.pic = pygame.image.load('images/Bloopera1.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def update_pos(self):
        self.x += self.settings.blooper_speed * self.x_direction
        self.rect.x = self.x

    def update_image(self):
        # Animation tied into movement
        if self.frame is 1:
            self.height = self.settings.bloopera2_height
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.pic = pygame.image.load('images/Bloopera2.png')
            self.image = pygame.transform.scale(self.pic, (self.width, self.height))
            self.frame = 2
        elif self.frame is 2:
            self.height = self.settings.bloopera1_height
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.pic = pygame.image.load('images/Bloopera1.png')
            self.image = pygame.transform.scale(self.pic, (self.width, self.height))
            self.frame = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
