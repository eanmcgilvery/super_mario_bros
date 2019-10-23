import pygame
import sys
import random

# Import all enemies
from blooper import Blooper
from cheep_cheep import CheepCheep
from fake_bowser import FakeBowser
from goomba import Goomba
from koopa_troopa import KoopaTroopa
from piranha_plant import PiranhaPlant


def check_events(settings, screen, timers, enemies):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, timers, enemies)


def check_keydown_events(event, settings, screen, timers, enemies):
    # For testing
    if event.key == pygame.K_q:
        enemies.add(Goomba(settings, screen, 40, 40, 1))
    elif event.key == pygame.K_w:
        enemies.add(Goomba(settings, screen, 160, 40, 2))
    elif event.key == pygame.K_e:
        enemies.add(KoopaTroopa(settings, screen, 280, 40, 1))
    elif event.key == pygame.K_r:
        enemies.add(KoopaTroopa(settings, screen, 400, 40, 2))
    elif event.key == pygame.K_t:
        enemies.add(KoopaTroopa(settings, screen, 520, 40, 3))
    elif event.key == pygame.K_y:
        enemies.add(KoopaTroopa(settings, screen, 760, 40, 4))
    elif event.key == pygame.K_u:
        enemies.add(KoopaTroopa(settings, screen, 880, 40, 5))
    elif event.key == pygame.K_i:
        enemies.add(PiranhaPlant(settings, screen, timers, 1000, 40, 1))
    elif event.key == pygame.K_o:
        enemies.add(PiranhaPlant(settings, screen, timers, 40, 400, 2))
    elif event.key == pygame.K_p:
        enemies.add(CheepCheep(settings, screen, 160, 400, 1))
    elif event.key == pygame.K_a:
        enemies.add(CheepCheep(settings, screen, 280, 400, 2))
    elif event.key == pygame.K_s:
        enemies.add(CheepCheep(settings, screen, random.randint(0, 100), settings.screen_height, 3))
    elif event.key == pygame.K_d:
        enemies.add(Blooper(settings, screen, 520, 400, 1))
    elif event.key == pygame.K_f:
        enemies.add(FakeBowser(settings, screen, 760, 400, 1))


def update_screen(screen, enemies, timers):
    if timers.curtime - timers.last_display > timers.display_wait:
        timers.last_display = timers.curtime
        # Level 1-1 Background color
        screen.fill((170, 170, 255))
        for enemy in enemies:
            enemy.blitme()
        pygame.display.flip()


def update_animations(enemies, timers):
    if timers.curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        timers.last_enemy_animation = timers.curtime
        for enemy in enemies:
            enemy.update_image()


def update_pos(settings, enemies, timers):
    if timers.curtime - timers.last_move > timers.move_wait:
        timers.last_move = timers.curtime
        for enemy in enemies:
            enemy.update_pos()
            if enemy.rect.right < -50 or enemy.rect.top > settings.screen_height + 10:
                enemies.remove(enemy)
