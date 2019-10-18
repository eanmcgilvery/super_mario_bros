import pygame
from enemy import Enemy


class BulletBill(Enemy):
    def __init__(self, settings, screen, x, y):
        super(BulletBill, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.bullet_bill_width, settings.bullet_bill_height)
        self.pic = pygame.image.load('images/Bullet_Bill1.png')
        self.image = pygame.transform.scale(self.pic, (settings.bullet_bill_width, settings.bullet_bill_height))
