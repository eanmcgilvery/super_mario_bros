import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from timers import Timers
from level1_1 import Level1_1
from level1_1_hidden import Level1_1_hidden

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

    # Create a group to hold all objects and background
    objects = Group()
    background = Group()

    # Create first level
    levels = [Level1_1(settings, screen), Level1_1_hidden(settings, screen)]
    #levels[0].active = True
    #levels[0].generate_map(settings, screen, objects, background)
    #levels[0].enemy_spawn_triggers(enemies)
    #levels[0].background_sound(settings)

    levels[1].generate_map(settings, screen, objects, background)
    levels[1].background_sound(settings)

    while True:
        timers.curtime = pygame.time.get_ticks()
        gf.check_events(settings, screen, timers, enemies, objects, background, levels)
        gf.update_pos(settings, timers, enemies, objects, background, levels)
        gf.update_animations(enemies, timers, objects)
        gf.update_screen(screen, enemies, timers, objects, background, levels)


run_game()
