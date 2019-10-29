from pygame.sprite import Sprite


class Object(Sprite):
    def __init__(self, settings, screen, x, y, otype):
        super(Object, self).__init__()
        self.settings = settings
        self.screen = screen

        # Store exact position
        self.x = x
        self.y = y

        # Initial movement direction is left
        self.x_direction = -1

        # Initially standing on ground
        self.y_velocity = 0

        # Place in animation
        self.frame = 1

        # Pipe Type
        self.otype = otype

        self.eliminated = False

    def move_with_screen(self, screen_x_move):
        self.x -= screen_x_move
        self.rect.x = self.x

    def update_pos(self, objects):
        self.x += 1