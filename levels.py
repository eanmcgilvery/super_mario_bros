class Level:
    def __init__(self, settings, screen, bg_color):
        super(Level, self).__init__()
        self.settings = settings
        self.screen = screen
        self.bg_color = bg_color

        self.active = False
        self.x_spawn_point = self.settings.screen_width + 200
