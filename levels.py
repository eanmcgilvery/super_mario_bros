class Level:
    def __init__(self, settings, screen, ui, timers, bg_color):
        super(Level, self).__init__()
        self.settings = settings
        self.screen = screen
        self.ui = ui
        self.timers = timers
        self.bg_color = bg_color

        self.active = True
        self.x_spawn_point = self.settings.screen_width + 200
