import pygame

# Import all enemies
from blooper import Blooper
from cheep_cheep import CheepCheep
from fake_bowser import FakeBowser
from goomba import Goomba
from koopa_troopa import KoopaTroopa
from piranha_plant import PiranhaPlant


def update_animations(timers):
    curtime = pygame.time.get_ticks()
    if curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        timers.last_enemy_animation = curtime
        '''enemies.update_image()'''
