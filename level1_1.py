import pygame
import sys

from settings import Settings as s
from collider import Collider

class Level1_1:
    def __init__(self):

        self.setup_backgroud()


    def setup_background(self):
        """Setting up background"""

        self.background = pyame.image.load('image/level1_1.png')
        self.back_rect = self.background.get_rect()
        self.background = pygame.transform.scale(self.background, (int(self.back_rect.width*s.background_multipler), int(self.back_rect.height*s.background_multipler)))
        self.back_rect = self.background.get_rect()

        width = self.back_rect.width
        height = self.back_rect.height

        self.level = pygame.Suface((width, height)).convert()
        self.level_rect = self.level.get_rect()

        screen = pygame.display.set_mode(s.screen_size)
        screen_rect = screen.get_rect()

        self.viewport = screen_rect(bottom=self.level_rect.bottom)
        self.viewport.x = self.game.info['camera start x']


    def setup_ground(self):
        """Setting up invisible ground on top of background"""
        ground_rect1 = collider.Collider(0, s.ground_height, 2953, 60)
        ground_rect2 = collider.Collider(3048, s.ground_height, 635, 60)
        ground_rect3 = collider.Collider(3819, s.ground_height, 2735, 60)
        ground_rect4 = collider.Collider(6647, s.ground_height, 2300, 60)

        self.ground_group = pygame.sprite.Group(ground_rect1, ground_rect2, ground_rect3, ground_rect4)

    def setup_pipes(self):
        """Setting up invisible pipes on top of background"""
        pipe1 = collider.Collider(1202, 452, 83, 82)
        pipe2 = collider.Collider(1631, 409, 83, 140)
        pipe3 = collider.Collider(1973, 366, 83, 170)
        pipe4 = collider.Collider(2445, 366, 83, 170)
        pipe5 = collider.Collider(6989, 452, 83, 82)
        pipe6 = collider.Collider(7675, 452, 83, 82)

        self.pipe_group = pygame.sprite.Group(pipe1, pipe2, pipe3, pipe4, pipe5, pipe6)

    def setup_steps(self):
        """Setting up the steps"""
        step1 = collider.Collider(5745, 495, 40, 44)
        step2 = collider.Collider(5788, 452, 40, 44)
        step3 = collider.Collider(5831, 409, 40, 44)
        step4 = collider.Collider(5874, 366, 40, 176)

        step5 = collider.Collider(6001, 366, 40, 176)
        step6 = collider.Collider(6044, 408, 40, 40)
        step7 = collider.Collider(6087, 452, 40, 40)
        step8 = collider.Collider(6130, 495, 40, 40)

        step9 = collider.Collider(6345, 495, 40, 40)
        step10 = collider.Collider(6388, 452, 40, 40)
        step11 = collider.Collider(6431, 409, 40, 40)
        step12 = collider.Collider(6474, 366, 40, 40)
        step13 = collider.Collider(6517, 366, 40, 176)

        step14 = collider.Collider(6644, 366, 40, 176)
        step15 = collider.Collider(6687, 408, 40, 40)
        step16 = collider.Collider(6728, 452, 40, 40)
        step17 = collider.Collider(6771, 495, 40, 40)
        step18 = collider.Collider(7760, 495, 40, 40)
        step19 = collider.Collider(7803, 452, 40, 40)
        step20 = collider.Collider(7845, 409, 40, 40)
        step21 = collider.Collider(7888, 366, 40, 40)
        step22 = collider.Collider(7931, 323, 40, 40)
        step23 = collider.Collider(7974, 280, 40, 40)
        step24 = collider.Collider(8017, 237, 40, 40)
        step25 = collider.Collider(8060, 194, 40, 40)
        step26 = collider.Collider(8103, 194, 40, 360)

        step27 = collider.Collider(8488, 495, 40, 40)

        self.step_group = pg.sprite.Group(step1, step2, step3, step4, step5, step6, step7, step8, step9, step10, step11, step12, step13, step14,
                                          step15, step16,step17, step18,step19, step20, step21, step22, step23, step24, step25, step26, step27)

