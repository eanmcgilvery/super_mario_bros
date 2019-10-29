import pygame as pg
import spritesheet
from settings import Settings as sy


# Class that holds all of the attributes of our hero, Mario
class Mario(pg.sprite.Sprite):
    def __init__(self, settings, screen):
        pg.sprite.Sprite.__init__(self)

        self.jump_ = False
        self.move_right = False
        self.move_left = False
        self.crouch = False
        self.max_x_vel = 100
        self.curtime = pg.time.get_ticks()

        self.allow_jump = True
        self.screen = screen
        self.settings = settings

        # Setup containers to hold the differing animations

        self.right_frames = [pg.image.load('images/mario_images/small_right/0.png').convert_alpha(),
                             pg.image.load('images/mario_images/small_right/1.png').convert_alpha(),
                             pg.image.load('images/mario_images/small_right/2.png').convert_alpha(),
                             pg.image.load('images/mario_images/small_right/3.png').convert_alpha()]

        self.left_frames = []
        for frame in self.right_frames:
            image = pg.transform.flip(frame, True, False)
            self.left_frames.append(image)

        self.right_big_normal_frames = [pg.image.load('images/mario_images/big_right/0.png').convert_alpha(),
                                        pg.image.load('images/mario_images/big_right/1.png').convert_alpha(),
                                        pg.image.load('images/mario_images/big_right/2.png').convert_alpha(),
                                        pg.image.load('images/mario_images/big_right/3.png').convert_alpha()]

        self.left_big_normal_frames = []
        for frame in self.right_big_normal_frames:
            image = pg.transform.flip(frame, True, False)
            self.left_frames.append(image)

        self.right_fire_frames = [pg.image.load('images/mario_images/small_fire_right/0.png').convert_alpha(),
                                  pg.image.load('images/mario_images/small_fire_right/1.png').convert_alpha(),
                                  pg.image.load('images/mario_images/small_fire_right/2.png').convert_alpha(),
                                  pg.image.load('images/mario_images/small_fire_right/3.png').convert_alpha()]

        self.left_fire_frames = []
        for frame in self.right_fire_frames:
            image = pg.transform.flip(frame, True, False)
            self.left_fire_frames.append(image)

        # Variables that will update mario's speed

        self.y_velocity = 0
        self.x_velocity = 0

        # Size of Mario
        self.width = settings.mario_small_width
        self.height = settings.mario_small_height

        # Image list we will index through for animation
        self.index = 0
        self.image = pg.transform.scale(self.right_frames[self.index], (self.width, self.height))
        self.rect = pg.Rect(100, 500, self.width, self.height)

        self.x = self.rect.x = 100
        self.y = self.rect.y = self.settings.screen_height - 500

        self.center = float(self.rect.centerx)

        # Jumping attributes
        self.isJump = False
        self.jumpCount = 10

        self.facing_right = True
        self.crouching = False
        self.fire = False
        self.invincible = False
        self.super_size = False
        self.jump_denied = False
        self.death = False

    def animation(self):
        """Return the correct images of Mario to animate through"""
        if self.facing_right and not self.invincible and not self.fire and not self.super_size:
            self.image = self.right_frames[self.index]

        # Regular mario facing left
        elif not self.facing_right and not self.invincible and not self.fire and not self.super_size:
            self.image = pg.transform.scale(self.left_frames[self.index], (self.width, self.height))

    def death(self):
        pass

    def check_collisions(self, enemies, objects):
        if not self.death:
            for object in objects:
                if self.rect.colliderect(object):
                    if self.rect.bottom > object.rect.top and self.y_velocity >= self.rect.bottom - object.rect.top:  # Reposition goomba to the top of the object
                        self.y = object.rect.top - self.height
                        self.y_velocity = 0
                    elif object.rect.bottom > self.rect.top and self.y_velocity * -1 >= object.rect.bottom - self.rect.top:  # Reposition to the bottom
                        self.y = object.rect.bottom
                        self.y_velocity = 0
                    elif self.rect.right - object.rect.left < object.rect.right - self.rect.left:  # Reposition to the left
                        self.move_right = False
                    else:  # Reposition to the right
                        self.move_left = False
                    self.rect.x = self.x
                    self.rect.y = self.y

    def animation_speed(self):
        """Used to make walking animation speed be in relation to
        Mario's x-vel"""
        if self.x_velocity == 0:
            animation_speed = 130
        elif self.x_velocity > 0:
            animation_speed = 130 - (self.x_velocity * 13)
        else:
            animation_speed = 130 - (self.x_velocity * 13 * -1)

        return animation_speed

    def upTime(self):
        """Called when Mario is in a JUMP state."""
        if self.jumpCount >= -10:
            if self.jumpCount < 0:
                neg = -1
                self.y -= self.jumpCount**2 * 0.1 * neg
                self.jumpCount -= 1
            else:
                self.isJump = False
                self.jumpCount = 10

    def update_pos(self, enemies, objects, settings):
        if not self.death:
            # Constantly add a downward gravity force
            self.y_velocity += self.settings.fall_acceleration
            self.y += self.y_velocity
            self.rect.x = self.x
            self.rect.y = self.y

            # Move right or left
            if self.move_right:
                self.x += settings.WALK_SPEED
            elif self.move_left and self.rect.left > 0:
                self.x -= settings.WALK_SPEED

            # Jump with spacebar
            if self.jump_:
                self.upTime()
            self.check_collisions(enemies, objects)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
