from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, settings, screen, x, y):
        super(Enemy, self).__init__()
        self.settings = settings
        self.screen = screen

        # Store exact position
        self.x = x
        self.y = y

        # Initial movement direction is left and up
        self.x_direction = -1
        self.y_direction = -1

        # Place in animation
        self.frame = 1
