import pygame
from object import Object

class Coin(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Coin, self).__init__(settings, screen, x, y, otype)

        """otype 1: blinking coin, otype 2: spinning coin..."""

        if self.otype is 1:
            self.pic = pygame.image.load('images/blink_coin1.png')
            self.rect = pygame.Rect(x, y, settings.coin_width, settings.coin_height)
            self.image = pygame.transform.scale(self.pic, (settings.coin_width, settings.coin_height))
        elif self.otype is 2:
            self.pic = pygame.image.load('images/coin1.png')
            self.rect = pygame.Rect(x, y, settings.coin_width, settings.coin_height)
            self.image = pygame.transform.scale(self.pic, (settings.coin_width, settings.coin_height))


    def update_image(self):
        # Animation
        if self.otype is 1:
            if self.frame is 1:
                self.pic = pygame.image.load('images/blink_coin1.png')
                self.frame = 2
                self.image = pygame.transform.scale(self.pic, (self.settings.brick_lenth, self.settings.brick_lenth))
            elif self.frame is 2:
                self.pic = pygame.image.load('images/blink_coin2.png')
                self.frame = 3
                self.image = pygame.transform.scale(self.pic, (self.settings.brick_lenth, self.settings.brick_lenth))
            elif self.frame is 3:
                self.pic = pygame.image.load('images/blink_coin3.png')
                self.frame = 1
                self.image = pygame.transform.scale(self.pic, (self.settings.brick_lenth, self.settings.brick_lenth))
        elif self.otype is 2:
            if self.frame is 1:
                self.pic = pygame.image.load('images/coin1.png')
                self.frame = 2
                self.image = pygame.transform.scale(self.pic, (self.settings.brick_lenth, self.settings.brick_lenth))
            elif self.frame is 2:
                self.pic = pygame.image.load('images/coin2.png')
                self.frame = 3
                self.image = pygame.transform.scale(self.pic, (int(self.settings.spin_coin_width), self.settings.spin_coin_height))
            elif self.frame is 3:
                self.pic = pygame.image.load('images/coin3.png')
                self.frame = 1
                self.image = pygame.transform.scale(self.pic, (int(self.settings.spin_coin_width), self.settings.brick_lenth))

        #if self.otype is 2:
        #    if self.frame is 2 or 3:
        #        self.image = pygame.transform.scale(self.pic, (int(self.settings.spin_coin_width), self.settings.spin_coin_height))
        #else:
        #    self.image = pygame.transform.scale(self.pic, (self.settings.brick_lenth, self.settings.brick_lenth))

    def update_pos(self):
        self.x -= 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)