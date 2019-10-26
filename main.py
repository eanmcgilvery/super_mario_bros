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
    #map = pygame.display.get_surface()
    pygame.display.set_caption("Super Mario Bros")
    clock = pygame.time.Clock()

    # Create our timers
    timers = Timers()

    # Create a group to hold all enemies
    enemies = Group()

    # Create a group to hold all objects and background
    objects = Group()
    background = Group()

    #bg1 = pygame.image.load('images/level1_1.png').convert()
    #bg = pygame.transform.scale(bg1, (settings.map_width, settings.map_height))
    #bgx = 0
    #bgx2 = bg.get_width()
    #speed = 30
    gf.generate_map_1_1(settings, screen, objects, background)
    # Start the main loop for the game.
    while True:
        #gf.redrawWindow(screen, map, bgx, bgx2)
        ##clock.tick(speed)
        #bgx -= 0
        #bgx2 -= 0
        #if bgx < bg.get_width() * -1:
        #    bgx = bg.get_width()
        #if bgx2 < bg.get_width() * -1:
        #    bgx2 = bg.get_width()

        timers.curtime = pygame.time.get_ticks()
        #gf.generate_map_1_1(settings, screen, objects)
        gf.check_events(settings, screen, timers, enemies, objects, background)
        gf.update_pos(settings, timers, enemies, objects)
        gf.update_animations(enemies, timers, objects)
        gf.update_screen(screen, enemies, timers, objects, background)



run_game()
