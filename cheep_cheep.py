import pygame
import random
from enemy import Enemy


class CheepCheep(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(CheepCheep, self).__init__(settings, screen, x, y, etype)

        """etype 1 is red cheep cheep, 2 is gray, 3 is jumping (jumping cheep cheeps are just red ones facing right)"""
        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.cheep_width, settings.cheep_height)
        if self.etype is 1:
            self.pic = pygame.image.load('images/Cheep_cheep1a1.png')
        elif self.etype is 2:
            self.pic = pygame.image.load('images/Cheep_cheep2a1.png')
        elif self.etype is 3:
            self.pic = pygame.image.load('images/Cheep_cheep3a1.png')
        self.image = pygame.transform.scale(self.pic, (settings.cheep_width, settings.cheep_height))

        # type 3 cheep cheeps only move right
        if self.etype is 3:
            self.x_speed = random.randint(20, 30)
            self.y_speed = random.randint(60, 70)
            self.x_direction = 1

    def update_pos(self):
        """Each type of cheep cheep moves differently"""
        # type 1 moves left and randomly up or down
        if self.etype is 1:
            self.x += self.settings.cheep_speed * self.x_direction
        elif self.etype is 2:   # type 2 moves the same as 1 but at half the speed
            self.x += (self.settings.cheep_speed / 2) * self.x_direction
        elif self.etype is 3:   # type 3 moves with high random speeds
            self.x += self.x_speed * self.x_direction
        self.rect.x = self.x

    def update_image(self):
        # Alternate normal alive animation
        if self.frame is 1:
            if self.etype is 1:
                self.pic = pygame.image.load('images/Cheep_cheep1a2.png')
            elif self.etype is 2:
                self.pic = pygame.image.load('images/Cheep_cheep2a2.png')
            elif self.etype is 3:
                self.pic = pygame.image.load('images/Cheep_cheep3a2.png')
            self.frame = 2
        elif self.frame is 2:
            if self.etype is 1:
                self.pic = pygame.image.load('images/Cheep_cheep1a1.png')
            elif self.etype is 2:
                self.pic = pygame.image.load('images/Cheep_cheep2a1.png')
            elif self.etype is 3:
                self.pic = pygame.image.load('images/Cheep_cheep3a1.png')
            self.frame = 1
        self.image = pygame.transform.scale(self.pic, (self.settings.cheep_width, self.settings.cheep_height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
