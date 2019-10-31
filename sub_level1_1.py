import pygame

from levels import Level

from brick import Brick
from pipe import Pipe
from coin import Coin


class SubLevel1_1(Level):
    def __init__(self, settings, screen, enemies, objects, background, mario, ui, timers):
        super(SubLevel1_1, self).__init__(settings, screen, ui, timers, bg_color=(0, 0, 0))

        self.pipe_warp1_x = self.settings.brick_lenth * 13 - 4
        self.pipe_warp1 = pygame.Rect(self.pipe_warp1_x, self.settings.ground_level - self.settings.pipe1_1_height, 2, self.settings.pipe1_1_height)

        self.generate_map(settings, screen, objects, background, mario)
        self.background_sound()

    def generate_ground(self, settings, screen, objects):
        for x in range(17):
            objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 5))
            objects.add(
                Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 5))

    def background_sound(self):
        pygame.mixer.music.load('sounds/underground.wav')
        pygame.mixer.music.play(-1, 0.0)

    def generate_map(self, settings, screen, objects, background, mario):
        mario.x = 40
        mario.y = 0
        mario.rect.x = mario.x
        mario.rect.y = mario.y
        self.generate_ground(settings, screen, objects)

        objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 4, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 5, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 6, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 7, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 8, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 9, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 10, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 11, 6))

        objects.add(Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth, 6))

        objects.add(
            Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 2, 6))

        objects.add(
            Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 3, 6))

        objects.add(
            Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 11, 6))

        objects.add(
            Coin(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 4, 1))

        objects.add(
            Coin(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 6, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 6, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 6, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 6, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 6, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 6, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 6, 1))

        objects.add(
            Coin(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Coin(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 8, 1))

        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 13, settings.ground_level - settings.pipe1_1_height, 4))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 2, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 3, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 4, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 5, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 6, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 7, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 8, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 9, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 10, 6))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 11, 6))

    def warp_triggers(self, mario_):
        if self.pipe_warp1.colliderect(mario_) and mario_.move_right:
            self.active = False
            self.settings.level_num = 0
            self.settings.screen_pos = 0

    def trigger_move(self, screen_x_move):
        self.pipe_warp1_x -= screen_x_move
        self.pipe_warp1.x = self.pipe_warp1_x
