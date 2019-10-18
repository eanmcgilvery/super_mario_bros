import pygame

# Import all enemies
from blooper import Blooper
from bullet_bill import BulletBill
from buzzy_beetle import BuzzyBeetle
from cheep_cheep import CheepCheep
from goomba import Goomba
from hammer_bro import HammerBro
from koopa_troopa import KoopaTroopa
from lakitu import Lakitu
from piranha_plant import PiranhaPlant
from spiny import Spiny


def update_animations(timers):
    curtime = pygame.time.get_ticks()
    if curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        timers.last_enemy_animation = curtime
        '''enemies.update_image()'''
