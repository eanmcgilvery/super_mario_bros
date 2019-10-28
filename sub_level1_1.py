from levels import Level

from brick import Brick
from pipe import Pipe
from coin import Coin


class SubLevel1_1(Level):
    def __init__(self, settings, screen):
        super(SubLevel1_1, self).__init__(settings, screen, bg_color=(0, 0, 0))

    def generate_map(self, settings, screen, objects, background):
        pass

    def enemy_spawn_triggers(self, enemies):
        pass
