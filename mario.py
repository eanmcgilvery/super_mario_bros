import pygame as pygame
import spritesheet
from settings import Settings


# Class that holds all of the attributes of our hero, Mario
class Mario(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.right_frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.physics()
        self.state()
        self.load_spritesheet()



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

    def load_spritesheet(self):
        """Extracts Mario images from his sprite sheet and assigns
        them to appropriate lists"""
        self.right_frames = []
        self.left_frames = []

        self.right_small_normal_frames = []
        self.left_small_normal_frames = []
        self.right_small_green_frames = []
        self.left_small_green_frames = []
        self.right_small_red_frames = []
        self.left_small_red_frames = []
        self.right_small_black_frames = []
        self.left_small_black_frames = []

        self.right_big_normal_frames = []
        self.left_big_normal_frames = []
        self.right_big_green_frames = []
        self.left_big_green_frames = []
        self.right_big_red_frames = []
        self.left_big_red_frames = []
        self.right_big_black_frames = []
        self.left_big_black_frames = []

        self.right_fire_frames = []
        self.left_fire_frames = []


        #Images for normal small mario#
        self.right_small_normal_frames.append(
            self.image_at(178, 32, 12, 16))  # Right [0]
        self.right_small_normal_frames.append(
            self.get_image(80,  32, 15, 16))  # Right walking 1 [1]
        self.right_small_normal_frames.append(
            self.get_image(96,  32, 16, 16))  # Right walking 2 [2]
        self.right_small_normal_frames.append(
            self.get_image(112,  32, 16, 16))  # Right walking 3 [3]
        self.right_small_normal_frames.append(
            self.get_image(144, 32, 16, 16))  # Right jump [4]
        self.right_small_normal_frames.append(
            self.get_image(130, 32, 14, 16))  # Right skid [5]
        self.right_small_normal_frames.append(
            self.get_image(160, 32, 15, 16))  # Death frame [6]
        self.right_small_normal_frames.append(
            self.get_image(320, 8, 16, 24))  # Transition small to big [7]
        self.right_small_normal_frames.append(
            self.get_image(241, 33, 16, 16))  # Transition big to small [8]
        self.right_small_normal_frames.append(
            self.get_image(194, 32, 12, 16))  # Frame 1 of flag pole Slide [9]
        self.right_small_normal_frames.append(
            self.get_image(210, 33, 12, 16))  # Frame 2 of flag pole slide [10]
