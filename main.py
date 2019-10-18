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
    bullet_bills = Group()
    buzzy_beetles = Group()
    cheep_cheeps = Group()
    goombas = Group()
    hammer_bros = Group()
    koopa_troopas = Group()
    lakitus = Group()
    piranha_plants = Group()
    spinies = Group()


run_game()
