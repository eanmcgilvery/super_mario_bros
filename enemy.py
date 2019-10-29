from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, settings, screen, timers, x, y, etype, ename):
        super(Enemy, self).__init__()
        self.settings = settings
        self.screen = screen
        self.timers = timers

        # Store exact position
        self.x = x
        self.y = y

        # Identify which type the enemy is
        self.etype = etype
        self.ename = ename

        # Initial movement direction is left
        self.x_direction = -1

        # Initially standing on ground
        self.y_velocity = 0

        # Place in animation
        self.frame = 1

        # Must use update_image when an enemy dies
        self.is_dead = False
        self.eliminated = False

    def move_with_screen(self, screen_x_move):
        self.x -= screen_x_move
        self.rect.x = self.x
