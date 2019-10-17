import pygame
from pygame.sprite import Sprite
from settings import Settings

# Class that gold all of the attributes of our hero, Mario
class Mario(Sprite):
    def __init__(self, settings):
        super(Mario, self).__init__()
            self.image = self.right_frames[self.frame_index]
            self.rect = self.image.get_rect()
            self.physics
            self.state()

    # Defining the physics for when Mario moving
    def physics(self):
        self.x_dir = 0
        self.y_dir = 0

        self.max_x = MAX_WALKING_SPEED
        self.max_y = MAX_HEIGHT_SPEED

        self.fall_speed = MAX_FALL_SPEED

    # Function that contains all the booleans for Mario
    def state(self):
        self.facing_right = True
        self.crouching = False

        # Set to True when jump is initiated.
        self.jump_denied = False

        # States of Mario
        self.fire = False
        self.invincible = False
