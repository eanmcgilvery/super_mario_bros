from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, settings, screen, x, y, etype):
        super(Enemy, self).__init__()
        self.settings = settings
        self.screen = screen

        # Store exact position
        self.x = x
        self.y = y

        # Identify which type the enemy is
        self.etype = etype

        # Initial movement direction is left
        self.x_direction = -1

        # Initially standing on ground
        self.y_velocity = 0

        # Place in animation
        self.frame = 1
