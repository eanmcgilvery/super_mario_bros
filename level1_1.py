from levels import Level
import pygame
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

# Import the enemies that will be used
from goomba import Goomba
from koopa_troopa import KoopaTroopa


class Level1_1(Level):
    def __init__(self, settings, screen, ui, timers):
        super(Level1_1, self).__init__(settings, screen, ui, timers, bg_color=(170, 170, 255))

        # Keep track of which enemies have spawned
        self.goomba1 = False
        self.goomba2 = False
        self.goomba3 = False
        self.goomba4 = False
        self.goomba5 = False
        self.goomba6 = False
        self.goomba7 = False
        self.goomba8 = False
        self.goomba9 = False
        self.goomba10 = False
        self.goomba11 = False
        self.goomba12 = False
        self.goomba13 = False
        self.goomba14 = False
        self.goomba15 = False
        self.koopa1 = False


    def generate_ground(self, settings, screen, objects):
        for x in range(70):
            objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
            objects.add(
                Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))
        for x in range(72, 87):
            objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
            objects.add(
                Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))
        for x in range(90, 154):
            objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
            objects.add(
                Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))
        for x in range(156, 213):
            objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
            objects.add(
                Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))

    def generate_map(self, settings, screen, objects, background):

        self.generate_ground(settings, screen, objects)

        background.add(Hill(settings, screen, 0, settings.ground_level - settings.large_hill_height, 2))
        background.add(Cloud(settings, screen, settings.brick_lenth * 9, settings.brick_lenth * 3, 1))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 12, settings.ground_level - settings.brick_lenth, 3))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 16, settings.ground_level - settings.brick_lenth - 2, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 16, settings.ground_level - settings.brick_lenth * 4, 1))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 20, settings.ground_level - settings.brick_lenth * 15, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 22, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 20, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 21, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 22, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 23, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 24, settings.ground_level - settings.brick_lenth * 4, 3))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 23.5, settings.ground_level - settings.brick_lenth, 1))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 29, settings.ground_level - settings.brick_lenth * 2, 1))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 39, settings.ground_level - settings.brick_lenth * 3, 2))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 47, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 58, settings.ground_level - settings.brick_lenth * 4, 3))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 28, settings.ground_level - settings.brick_lenth * 12, 3))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 37, settings.ground_level - settings.brick_lenth * 15, 2))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 41.5, settings.ground_level - settings.brick_lenth, 3))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 49, settings.ground_level - settings.large_hill_height - 2,
                 2))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 57, settings.ground_level - settings.brick_lenth * 15, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 65, settings.ground_level - settings.brick_lenth * 5, 1))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 60.5, settings.ground_level - settings.brick_lenth, 3))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 65, settings.ground_level - settings.small_hill_height, 1))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 68, settings.ground_level - settings.brick_lenth * 15, 1))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 72.5, settings.ground_level - settings.brick_lenth, 1))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 76, settings.ground_level - settings.brick_lenth * 13, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 78, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 79, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 80, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 81, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 82, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 83, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 84, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 85, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 86, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 87, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 88, settings.ground_level - settings.brick_lenth * 8, 3))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 85, settings.ground_level - settings.brick_lenth * 15, 2))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 92, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 93, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 94, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 95, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 95, settings.ground_level - settings.brick_lenth * 4, 3))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 90.5, settings.ground_level - settings.brick_lenth, 2))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 97, settings.ground_level - settings.large_hill_height - 2,
                 2))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 101, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 102, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 107, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 110, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 113, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 110, settings.ground_level - settings.brick_lenth * 8, 1))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 106, settings.ground_level - settings.brick_lenth * 11, 1))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 108.5, settings.ground_level - settings.brick_lenth, 3))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 113, settings.ground_level - settings.small_hill_height, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 119, settings.ground_level - settings.brick_lenth * 4, 3))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 116, settings.ground_level - settings.brick_lenth * 12, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 122, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 123, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 124, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 129, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 130, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 131, settings.ground_level - settings.brick_lenth * 8, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 132, settings.ground_level - settings.brick_lenth * 8, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 130, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 131, settings.ground_level - settings.brick_lenth * 4, 3))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 120.5, settings.ground_level - settings.brick_lenth, 1))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 124, settings.ground_level - settings.brick_lenth * 11, 3))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 133, settings.ground_level - settings.brick_lenth * 13, 2))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 138.5, settings.ground_level - settings.brick_lenth, 2))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 145, settings.ground_level - settings.large_hill_height, 2))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 11, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 135, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 136, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 137, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 136, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 137, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 137, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 142, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 142, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 142, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 143, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 143, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 144, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 149, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 150, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 150, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 151, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 151, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 151, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 157, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 157, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 157, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 158, settings.ground_level - settings.brick_lenth * 1, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 158, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 159, settings.ground_level - settings.brick_lenth * 1, 4))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 161, settings.ground_level - settings.small_hill_height, 1))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 164, settings.ground_level - settings.brick_lenth * 13, 1))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 172, settings.ground_level - settings.brick_lenth * 11, 3))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 181, settings.ground_level - settings.brick_lenth * 13, 2))
        background.add(
            Cloud(settings, screen, settings.brick_lenth * 201, settings.ground_level - settings.brick_lenth * 11, 1))
        background.add(
            Bush(settings, screen, settings.brick_lenth * 167.5, settings.ground_level - settings.brick_lenth, 1))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 193, settings.ground_level - settings.large_hill_height, 2))
        background.add(
            Hill(settings, screen, settings.brick_lenth * 209, settings.ground_level - settings.small_hill_height, 1))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 164, settings.ground_level - settings.brick_lenth * 2, 1))
        objects.add(
            Pipe(settings, screen, settings.brick_lenth * 180, settings.ground_level - settings.brick_lenth * 2, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 169, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 170, settings.ground_level - settings.brick_lenth * 4, 3))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 171, settings.ground_level - settings.brick_lenth * 4, 1))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 172, settings.ground_level - settings.brick_lenth * 4, 3))

        objects.add(
            Brick(settings, screen, settings.brick_lenth * 182, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 183, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 183, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 184, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 184, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 184, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 5, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 5, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 6, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 5, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 6, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 7, 4))

        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 5, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 6, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 7, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 8, 4))

        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 2, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 3, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 4, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 5, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 6, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 7, 4))
        objects.add(
            Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 8, 4))
        objects.add(
            Flag_Pole(settings, screen, settings.brick_lenth * 199, settings.ground_level - settings.flag_pole_height,
                      1))
        objects.add(
            Castle(settings, screen, settings.brick_lenth * 203, settings.ground_level - settings.small_castle_height,
                   1))

    def enemy_spawn_triggers(self, enemies):
        # Screen position should have the position of the left side of the screen saved
        if not self.goomba1:
            self.goomba1 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.settings.brick_lenth * 25,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba2 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 42:
            self.goomba2 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba3 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 56:
            self.goomba3 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba4 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 57:
            self.goomba4 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba5 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 82:
            self.goomba5 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.brick_lenth * 8 - self.settings.goomba_height,
                               1))
        if not self.goomba6 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 84:
            self.goomba6 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.brick_lenth * 8 - self.settings.goomba_height,
                               1))
        if not self.goomba7 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 100:
            self.goomba7 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba8 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 101:
            self.goomba8 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.koopa1 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 109:
            self.koopa1 = True
            enemies.add(KoopaTroopa(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                                    self.settings.ground_level - self.settings.koopa_height, 1))
        if not self.goomba9 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 118:
            self.goomba9 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba10 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 119:
            self.goomba10 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba11 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 128:
            self.goomba11 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba12 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 129:
            self.goomba12 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba13 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 131:
            self.goomba13 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba14 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 175:
            self.goomba14 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))
        if not self.goomba15 and self.settings.screen_pos + self.x_spawn_point > self.settings.brick_lenth * 176:
            self.goomba15 = True
            enemies.add(Goomba(self.settings, self.screen, self.ui, self.timers, self.x_spawn_point,
                               self.settings.ground_level - self.settings.goomba_height, 1))

    def background_sound(self, settings):
        settings.background_sound.play()
