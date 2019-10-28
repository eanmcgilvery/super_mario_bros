import pygame as pg
import spritesheet
from settings import Settings as sy

# Class that holds all of the attributes of our hero, Mario
class Mario(pg.sprite.Sprite):
    def __init__(self, settings, screen):
        pg.sprite.Sprite.__init__(self)

        self.max_x_vel = 100
        self.curtime = pg.time.get_ticks()
        self.allow_jump = False
        self.screen = screen
        self.settings = settings

        # Setup containers to hold the differing animations

        self.right_frames = [pg.image.load('images/mario_images/small_right/0.png').convert_alpha(),
                             pg.image.load('images/mario_images/small_right/1.png').convert_alpha(),
                             pg.image.load('images/mario_images/small_right/2.png').convert_alpha(),
                             pg.image.load('images/mario_images/small_right/3.png').convert_alpha()]

        self.left_frames = [pg.image.load('images/mario_images/small_right/0.png').convert_alpha(),
                            pg.image.load('images/mario_images/small_right/1.png').convert_alpha(),
                            pg.image.load('images/mario_images/small_right/2.png').convert_alpha(),
                            pg.image.load('images/mario_images/small_right/3.png').convert_alpha()]

        self.right_big_normal_frames = [pg.image.load('images/mario_images/big_right/0.png').convert_alpha(),
                                        pg.image.load('images/mario_images/big_right/1.png').convert_alpha(),
                                        pg.image.load('images/mario_images/big_right/2.png').convert_alpha(),
                                        pg.image.load('images/mario_images/big_right/3.png').convert_alpha()]

        self.left_big_normal_frames = [pg.image.load('images/mario_images/big_right/0.png').convert_alpha(),
                                       pg.image.load('images/mario_images/big_right/1.png').convert_alpha(),
                                       pg.image.load('images/mario_images/big_right/2.png').convert_alpha(),
                                       pg.image.load('images/mario_images/big_right/3.png').convert_alpha()]

        self.right_fire_frames = [pg.image.load('images/mario_images/small_fire_right/0.png').convert_alpha(),
                                  pg.image.load('images/mario_images/small_fire_right/1.png').convert_alpha(),
                                  pg.image.load('images/mario_images/small_fire_right/2.png').convert_alpha(),
                                  pg.image.load('images/mario_images/small_fire_right/3.png').convert_alpha()]

        self.left_fire_frames = [pg.image.load('images/mario_images/small_fire_right/0.png').convert_alpha(),
                                 pg.image.load('images/mario_images/small_fire_right/1.png').convert_alpha(),
                                 pg.image.load('images/mario_images/small_fire_right/2.png').convert_alpha(),
                                 pg.image.load('images/mario_images/small_fire_right/3.png').convert_alpha()]

        # Variables that will update mario's speed

        self.y_vel = 0
        self.x_vel = 0

        # Image list we will index through for animation
        self.index = 0
        self.image = self.right_frames[self.index]
        self.rect = self.image.get_rect()

        # Size of Mario
        self.width = settings.mario_small_width
        self.height = settings.mario_small_height

        #Marios staring position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.facing_right = True
        self.crouching = False
        self.fire = False
        self.invincible = False
        self.super_size = False
        self.jump_denied = False
        self.death = False

    def select_animation(self):
        """Return the correct images of Mario to animate through"""
        if self.facing_right and not self.invincible and not self.fire and not self.super_size:
            return self.right_frames

        # Regular mario facing left
        elif not self.facing_right and not self.invincible and not self.fire and not self.super_size:
            return self.left_frames

    def animation(self):
        self.image = self.select_animation()

    def animation_speed(self):
        """Used to make walking animation speed be in relation to
        Mario's x-vel"""
        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)

        return animation_speed

    def blitme(self):

        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def walk(self, settings):
        if self.index == 0:
            self.index += 1
            self.walking_timer = self.curtime
        else:
            if self.curtime - self.walking_timer > self.animation_speed():
                if self.index < 3:
                    self.index += 1
                else:
                    self.index = 1
                self.walking_timer = self.curtime

        self.facing_right = False
        if self.x_vel > 0:
            self.index = 5
            self.x_accel = settings.SMALL_TURNAROUND
        else:
            self.x_accel = settings.WALK_ACCEL

        if self.x_vel > (self.max_x_vel * -1):
            self.x_vel -= self.x_accel
            if self.x_vel > -0.5:
                self.x_vel = -0.5
        elif self.x_vel < (self.max_x_vel * -1):
            self.x_vel += self.x_accel
        pass

    def jumping(self, keys, fire_group):
        """Called when Mario is in a JUMP state."""
        pass
        self.index = 3

        self.gravity = sy.FALL_SPEED
        self.y_vel += self.gravity

        #self.check_to_allow_fireball(keys)

        if 0 <= self.y_vel < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if not self.facing_right:
            if self.x_vel > (self.max_x_vel * - 1):
                self.x_vel -= self.x_accel

        elif self.facing_right:
            if self.x_vel < self.max_x_vel:
                self.x_vel += self.x_accel
