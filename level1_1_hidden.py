from levels import Level

# Import all objects
from brick import Brick
from bush import Bush
from castle import Castle
from castle_flag import CastleFlag
from cloud import Cloud
from hill import Hill
from pipe import Pipe
from coin import Coin
from flag_pole import Flag_Pole

#


class Level1_1_hidden(Level):
    def __init__(self, settings, screen):
        super(Level1_1_hidden, self).__init__(settings, screen, bg_color=(0, 0, 0))

    def generate_ground(self, settings, screen, objects):
        for x in range(17):
            objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 5))
            objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 5))


    def generate_map(self, settings, screen, objects, background):

        self.generate_ground(settings, screen, objects)

        objects.add(Brick(settings,screen, 0, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 4, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 5, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 6, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 7, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 8, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 9, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 10, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(Brick(settings, screen, 0, settings.ground_level - settings.brick_lenth * 12, 6))

        objects.add(Brick(settings, screen, settings.brick_lenth * 4, settings.ground_level - settings.brick_lenth * 12, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 5, settings.ground_level - settings.brick_lenth * 12, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 6, settings.ground_level - settings.brick_lenth * 12, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 7, settings.ground_level - settings.brick_lenth * 12, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 8, settings.ground_level - settings.brick_lenth * 12, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 9, settings.ground_level - settings.brick_lenth * 12, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 10, settings.ground_level - settings.brick_lenth * 12, 6))
        objects.add(Brick(settings, screen, settings.brick_lenth * 11, settings.ground_level - settings.brick_lenth * 12, 6))

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
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 2, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 3, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 4, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 5, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 6, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 7, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 8, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 9, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 10, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 11, 6))
        objects.add(Pipe(settings, screen, settings.brick_lenth * 15, settings.ground_level - settings.brick_lenth * 12, 6))

    def background_sound(self, settings):
        settings.underground_sound.play()