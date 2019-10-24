import pygame
from object import Object

class Cloud(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Cloud, self).__init__(settings, screen, x, y, otype)

        # Rect, image, and initial position set up
        if self.otype is 1:
            self.pic = pygame.image.load('images/cloud1.png')
            self.rect = pygame.Rect(x, y, settings.small_cloud_width, settings.small_cloud_height)
            self.image = pygame.transform.scale(self.pic, (settings.small_cloud_width, settings.small_cloud_height))
        elif self.otype is 2:
            self.pic = pygame.image.load('images/cloud2.png')
            self.rect = pygame.Rect(x, y, settings.medium_cloud_width, settings.medium_cloud_height)
            self.image = pygame.transform.scale(self.pic, (settings.medium_cloud_width, settings.medium_cloud_height))
        elif self.otype is 3:
            self.pic = pygame.image.load('images/cloud3.png')
            self.rect = pygame.Rect(x, y, settings.large_cloud_width, settings.large_cloud_height)
            self.image = pygame.transform.scale(self.pic, (settings.large_cloud_width, settings.large_cloud_height))

    def update_image(self):
        self.image = self.image

    def blitme(self):
        self.screen.blit(self.image, self.rect)