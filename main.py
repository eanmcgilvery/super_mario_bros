import pygame
import game_functions as gf
from pygame.sprite import Group
from settings import Settings
from user_interface import UserInterface
from timers import Timers
from level1_1 import Level1_1
from sub_level1_1 import SubLevel1_1
from mario import Mario
from mushroom import Mushroom


def run_game():

    # Initialize pygame, settings, and screen object.
    pygame.init()
    settings = Settings()
    '''
    full_screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.Surface((settings.screen_width, settings.screen_height))
    
    After everything has been blit onto screen use:
    full_screen.blit(pygame.transform.scale(screen, (1980, 1080)), (0, 0))
    pygame.display.flip()
    '''
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    ui = UserInterface(settings, screen)
    pygame.display.set_caption("Super Mario Bros")

    # Create our timers
    timers = Timers()

    # Create a group to hold all enemies
    enemies = Group()

    # Create our Hero
    mario = Mario(settings, screen, ui, timers)

    # Create a group to hold all objects and background
    objects = Group()
    background = Group()
    items = Group()

    # Create first level
    levels = [Level1_1(settings, screen, ui, timers), SubLevel1_1(settings, screen, ui, timers)]
    levels[0].active = True
    levels[0].generate_map(settings, screen, objects, background)
    levels[0].enemy_spawn_triggers(enemies)
    levels[0].background_sound(settings)

    while True:
        timers.curtime = pygame.time.get_ticks()
        gf.check_events(settings, screen, ui, timers, enemies, objects, background, levels, mario, items)
        gf.update_pos(settings, timers, enemies, objects, background, levels, items, mario)
        gf.update_animations(enemies, timers, objects, mario, settings, items)
        gf.update_level_timer(ui, timers, mario)
        gf.update_screen(screen, ui, enemies, timers, objects, background, levels, mario, items)


run_game()
