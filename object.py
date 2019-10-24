from pygame.sprite import Sprite


class Object(Sprite):
    def __init__(self, settings, screen, x, y, otype):
        super(Object, self).__init__()
        self.settings = settings
        self.screen = screen

        # Store exact position
        self.x = x
        self.y = y

        # Place in animation
        self.frame = 1

        # Pipe Type
        self.otype = otype