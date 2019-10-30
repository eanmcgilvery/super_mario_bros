from levels import Level

from brick import Brick
from pipe import Pipe
from coin import Coin


def generate_ground(settings, screen, objects):
    for x in range(17):
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 5))
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 5))


def background_sound(settings):
    settings.underground_sound.play()


def generate_map(settings, screen, objects):

    generate_ground(settings, screen, objects)

    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 2, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 3, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 4, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 5, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 6, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 7, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 8, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 9, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 10, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 0, settings.ground_level - settings.brick_lenth * 11, 6))

    objects.add(Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth, 6))

    objects.add(Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 2, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 2, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 2, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 2, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 2, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 2, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 2, 6))

    objects.add(Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 3, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 3, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 3, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 3, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 3, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 3, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 3, 6))

    objects.add(Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 11, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 11, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 11, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 11, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 11, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 11, 6))
    objects.add(Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 11, 6))

    objects.add(Coin(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 4, 1))

    objects.add(Coin(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 6, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 6, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 6, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 6, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 6, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 6, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 6, 1))

    objects.add(Coin(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Coin(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 8, 1))

    objects.add(Pipe(settings, screen, settings.brick_lenth * 13, settings.ground_level - settings.pipe1_1_height, 4))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 2, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 3, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 4, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 5, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 6, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 7, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 8, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 9, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 10, 6))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.pipe1_3_height * 11, 6))


class SubLevel1_1(Level):
    def __init__(self, settings, screen, ui, timers):
        super(SubLevel1_1, self).__init__(settings, screen, ui, timers, bg_color=(0, 0, 0))
