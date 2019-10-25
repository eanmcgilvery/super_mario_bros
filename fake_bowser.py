import pygame
import random
from enemy import Enemy


class FakeBowser(Enemy):
    def __init__(self, settings, screen, timers, x, y, etype):
        super(FakeBowser, self).__init__(settings, screen, x, y, etype, ename="fake_bowser")
        self.timers = timers

        # Rect, image, and initial position set up
        self.width = settings.fake_bowser_width
        self.height = settings.fake_bowser_height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.pic = pygame.image.load('images/Fake_Bowsera1l.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))
        self.pos = self.settings.fake_bowser_pos
        self.last_move = self.timers.curtime

        # Always faces mario regardless of which direction he moves
        self.facing_left = True

        # Can take a lot of hits before dying
        self.health = 10

    def update_pos(self, objects):
        self.x += self.settings.fake_bowser_speed * self.x_direction
        self.pos += self.settings.fake_bowser_speed * self.x_direction
        if self.pos < self.settings.fake_bowser_leash[0] or self.pos > self.settings.fake_bowser_leash[1]:
            self.x_direction *= -1
        if self.y_velocity is 0 and self.timers.curtime - self.last_move > self.timers.fake_bowser_jump_wait:
            self.last_move = self.timers.curtime
            self.timers.fake_bowser_jump_wait = random.randint(5000, 10000)
            self.y_velocity += self.settings.enemy_jump_speed
        self.y_velocity += self.settings.fall_acceleration
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
        self.check_collisions(objects)

    def update_image(self, changeframe):
        # Alternate normal alive animation
        if self.facing_left:
            if self.frame is 1:
                self.pic = pygame.image.load('images/Fake_Bowsera2l.png')
                self.frame = 2
            elif self.frame is 2:
                self.pic = pygame.image.load('images/Fake_Bowsera1l.png')
                self.frame = 1
        elif not self.facing_left:
            if self.frame is 1:
                self.pic = pygame.image.load('images/Fake_Bowsera2r.png')
                self.frame = 2
            elif self.frame is 2:
                self.pic = pygame.image.load('images/Fake_Bowsera1r.png')
                self.frame = 1
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def check_collisions(self, objects):
        for object in objects:
            if self.rect.colliderect(object):
                if self.rect.bottom > object.rect.top and self.y_velocity >= self.rect.bottom - object.rect.top:  # Reposition fake bowser to the top of the object
                    self.y = object.rect.top - self.height
                    self.y_velocity = 0
                self.rect.y = self.y

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.is_dead = True

    def blitme(self):
        self.screen.blit(self.image, self.rect)
