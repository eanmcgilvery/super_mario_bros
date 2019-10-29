import pygame


class UserInterface:
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen

        self.font = pygame.font.SysFont(None, 40)
        self.white = (255, 255, 255)

        self.score_text = "SCORE"
        self.score = 0

        self.time_text = "TIME"
        self.time = 400

        self.world_text = "WORLD"
        self.world = "1-1"

        self.coins_text = "COINS"
        self.coins = 0

        self.lives_text = "LIVES"
        self.lives = 3

        self.text = [self.score_text, self.time_text, self.world_text, self.coins_text, self.lives_text]
        self.info_text = [self.score, self.time, self.world, self.coins, self.lives]

    def blitme(self):
        for x in range(5):
            textobj = self.font.render(self.text[x], 1, self.white)
            textrect = textobj.get_rect()
            textrect.topleft = 40 + ((self.settings.screen_width / 5) * x), 40
            self.screen.blit(textobj, textrect)
            textobj = self.font.render(str(self.info_text[x]), 1, self.white)
            textrect = textobj.get_rect()
            textrect.topleft = 40 + ((self.settings.screen_width / 5) * x), 80
            self.screen.blit(textobj, textrect)
