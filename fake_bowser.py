import pygame
import random
from enemy import Enemy


class FakeBowser(Enemy):
    def __init__(self, settings, screen, timers, x, y, etype):
        super(FakeBowser, self).__init__(settings, screen, timers, x, y, etype, ename="fake_bowser")

        # Rect, image, and initial position set up
        self.width = settings.fake_bowser_width
        self.height = settings.fake_bowser_height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.pic = pygame.image.load('images/Fake_Bowsera1l.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))
        self.pos = self.settings.fake_bowser_pos
        self.last_move = self.timers.curtime
        self.next_move = self.timers.curtime
        self.last_jump = self.timers.curtime
        self.grounded = False

        # Always faces mario regardless of which direction he moves
        self.facing_left = True

        # Can take a lot of hits before dying
        self.health = 10

    def update_pos(self, enemies, objects):
        if not self.eliminated:
            if self.grounded and self.pos < self.settings.fake_bowser_leash[0]:
                self.x_direction = 1
            elif self.grounded and self.pos > self.settings.fake_bowser_leash[1]:
                self.x_direction = -1
            if not self.grounded or self.timers.curtime - self.last_move > self.timers.fake_bowser_move_wait:
                self.x += self.settings.fake_bowser_speed * self.x_direction
                self.pos += self.settings.fake_bowser_speed * self.x_direction
                if self.timers.curtime - self.next_move > self.timers.fake_bowser_next_move_wait:
                    self.timers.fake_bowser_move_wait = random.randint(2000, 4000)
                    self.timers.fake_bowser_next_move_wait = self.timers.fake_bowser_move_wait + random.randint(1000, 3000)
                    self.last_move = self.timers.curtime
                    self.next_move = self.timers.curtime
            if self.y_velocity is 0 and self.timers.curtime - self.last_jump > self.timers.fake_bowser_jump_wait:
                self.last_jump = self.timers.curtime
                self.timers.fake_bowser_jump_wait = random.randint(5000, 10000)
                self.y_velocity += self.settings.enemy_jump_speed
            self.y_velocity += self.settings.fall_acceleration
            self.y += self.y_velocity
            self.rect.x = self.x
            self.rect.y = self.y
            self.check_collisions(objects)
        else:
            self.y_velocity += self.settings.fall_acceleration
            self.y += self.y_velocity
            self.rect.y = self.y

    def update_image(self, changeframe):
        if not self.eliminated:
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
        if not self.eliminated:
            self.grounded = False
            for object in objects:
                if self.rect.colliderect(object):
                    if self.rect.bottom > object.rect.top and self.y_velocity >= self.rect.bottom - object.rect.top:  # Reposition fake bowser to the top of the object
                        self.y = object.rect.top - self.height
                        self.y_velocity = 0
                        self.grounded = True
                    self.rect.y = self.y

    def take_damage(self):
        self.health -= 1
        if self.health <= 0:
            self.is_dead = True
            self.eliminate()

    def eliminate(self):
        self.is_dead = True
        self.eliminated = True
        if self.y_velocity < 0:
            self.y_velocity = 0
        if self.facing_left:
            self.pic = pygame.image.load('images/Fake_Bowserdl.png')
        elif not self.facing_left:
            self.pic = pygame.image.load('images/Fake_Bowserdr.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
