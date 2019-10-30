import pygame
import random
from enemy import Enemy


class CheepCheep(Enemy):
    def __init__(self, settings, screen, ui, timers, x, y, etype):
        super(CheepCheep, self).__init__(settings, screen, ui, timers, x, y, etype, ename="cheep_cheep")

        self.width = settings.cheep_width
        self.height = settings.cheep_height
        self.last_y_change = self.timers.curtime

        """etype 1 is red cheep cheep, 2 is gray, 3 is jumping (jumping cheep cheeps are just red ones facing right)"""
        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, self.width, self.height)
        if self.etype is 1:
            self.pic = pygame.image.load('images/Cheep_cheep1a1.png')
        elif self.etype is 2:
            self.pic = pygame.image.load('images/Cheep_cheep2a1.png')
        elif self.etype is 3:
            self.pic = pygame.image.load('images/Cheep_cheep3a1.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

        if self.etype is 1 or self.etype is 2:
            self.y_dir = random.randint(0, 2)
        elif self.etype is 3:  # type 3 cheep cheeps only move right
            self.x_speed = random.randint(5, 12)
            self.y_velocity = random.randint(18, 25) * -1
            self.x_direction = 1

    def update_pos(self):
        """Each type of cheep cheep moves differently"""
        # type 1 and 2 moves left and randomly up or down
        if self.eliminated:
            if self.etype is 1 or self.etype is 2:
                self.y_velocity += self.settings.swimming_fall_acceleration
            else:
                self.y_velocity += self.settings.fall_acceleration
        else:
            if self.etype is 1 or self.etype is 2:
                if self.timers.curtime - self.last_y_change > self.timers.cheep_y_change_wait:
                    self.y_dir = random.randint(0, 2)
                    self.last_y_change = self.timers.curtime
                if self.y_dir is 0:
                    if self.etype is 1:
                        self.y_velocity = self.settings.cheep_y_speed
                    else:
                        self.y_velocity = self.settings.cheep_y_speed / 2
                elif self.y_dir is 1:
                    self.y_velocity = 0
                elif self.y_dir is 2:
                    if self.etype is 1:
                        self.y_velocity = self.settings.cheep_y_speed * -1
                    else:
                        self.y_velocity = (self.settings.cheep_y_speed * -1) / 2
            if self.etype is 1:
                self.x += self.settings.cheep_speed * self.x_direction
            elif self.etype is 2:   # type 2 moves the same as 1 but at half the speed
                self.x += (self.settings.cheep_speed / 2) * self.x_direction
            elif self.etype is 3:   # type 3 moves with high random speeds
                self.x += self.x_speed * self.x_direction
                self.y_velocity += self.settings.swimming_fall_acceleration
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def update_image(self, changeframe):
        # Alternate normal alive animation
        if not self.eliminated:
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
            self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def take_damage(self):
        self.is_dead = True

    def eliminate(self):
        self.is_dead = True
        self.eliminated = True
        if self.y_velocity < 0:
            self.y_velocity = 0
        if self.etype is 1:
            self.pic = pygame.image.load('images/Cheep_cheep1d.png')
        elif self.etype is 2:
            self.pic = pygame.image.load('images/Cheep_cheep2d.png')
        elif self.etype is 3:
            self.pic = pygame.image.load('images/Cheep_cheep3d.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
