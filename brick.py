import pygame
from object import Object


class Brick(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Brick, self).__init__(settings, screen, x, y, otype)

        # Check if block is empty
        self.not_empty = True

        """Type 1: Question_brick, type 2: ground brick, type 3:breakable brick, type 4: steps, type 5: 1-2 ground brick
                type 6: 1-2 breakable brick"""
        self.rect = pygame.Rect(x, y, settings.brick_lenth, settings.brick_lenth)
        if self.otype is 1:
            self.pic = pygame.image.load('images/question1.png')
        elif self.otype is 2:
            self.pic = pygame.image.load('images/ground_brick.png')
        elif self.otype is 3:
            self.pic = pygame.image.load('images/brick.png')
        elif self.otype is 4:
            self.pic = pygame.image.load('images/step.png')
        elif self.otype is 5:
            self.pic = pygame.image.load('images/ground2_1.png')
        elif self.otype is 6:
            self.pic = pygame.image.load('images/brick2_2.png')

        self.image = pygame.transform.scale(self.pic, (settings.brick_lenth, settings.brick_lenth))

    def update_image(self):
        # Animation
        if self.otype is 1:
            # if self.not_emprty:
            if self.frame is 1:
                self.pic = pygame.image.load('images/question1.png')
                self.frame = 2
            elif self.frame is 2:
                self.pic = pygame.image.load('images/question2.png')
                self.frame = 3
            elif self.frame is 3:
                self.pic = pygame.image.load('images/question3.png')
                self.frame = 1
            # elif not self.not_empty:
            # self.pic = pygame.image.load('images/question4.png')

        self.image = pygame.transform.scale(self.pic, (self.settings.brick_lenth, self.settings.brick_lenth))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
