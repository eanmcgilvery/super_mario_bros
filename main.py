import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from timers import Timers


def run_game():

    # Initialize pygame, settings, and screen object.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    pygame.display.set_caption("Super Mario Bros")

    # Create our timers
    timers = Timers()

    # Create a group to hold all enemies
    enemies = Group()

    # Start the main loop for the game.
    while True:
        timers.curtime = pygame.time.get_ticks()
        gf.check_events(settings, screen, timers, enemies)
        gf.update_pos(settings, enemies, timers)
        gf.update_animations(enemies, timers)
        gf.update_screen(screen, enemies, timers)


run_game()
