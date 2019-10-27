import pygame
from object import Object

class Flag_Pole(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Flag_Pole, self).__init__(settings, screen, x, y, otype)

        # Rect, image, and initial position set up
        self.pic = pygame.image.load('images/flag_pole1.png')
        self.rect = pygame.Rect(x, y, int(self.settings.flag_pole_width), int(self.settings.flag_pole_height))
        self.image = pygame.transform.scale(self.pic, (int(self.settings.flag_pole_width), int(self.settings.flag_pole_height)))

    def update_image(self):
        # Animation
        if self.frame is 1:
            self.pic = pygame.image.load('images/flag_pole2.png')
            self.frame = 2
        elif self.frame is 2:
            self.pic = pygame.image.load('images/flag_pole3.png')
            self.frame = 3
        elif self.frame is 3:
            self.pic = pygame.image.load('images/flag_pole4.png')
            self.frame = 4
        elif self.frame is 4:
            self.pic = pygame.image.load('images/flag_pole5.png')
            self.frame = 1

        self.image = pygame.transform.scale(self.pic, (int(self.settings.flag_pole_width), int(self.settings.flag_pole_height)))


    def blitme(self):
        self.screen.blit(self.image, self.rect)