import pygame
from settings import Settings
from pygame.sprite import Group


def run_game():

    # Initialize pygame, settings, and screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Super Mario Bros")

    # Create a group for each enemy
    bloopers = Group()
    cheep_cheeps = Group()
    fake_bowsers = Group()
    goombas = Group()
    koopa_troopas = Group()
    piranha_plants = Group()
    enemies = [bloopers, cheep_cheeps, fake_bowsers, goombas, koopa_troopas, piranha_plants]


run_game()
