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

# Import all objects
from brick import Brick
from bush import Bush
from castle import Castle
from castle_flag import CastleFlag
from cloud import Cloud
from hill import Hill
from pipe import Pipe
from coin import Coin
from flag_pole import Flag_Pole


def check_events(settings, screen, timers, enemies, objects, background, levels):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, timers, enemies, objects, background, levels)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, screen, timers, enemies, objects, background, levels)


def check_keydown_events(event, settings, screen, timers, enemies, objects, background, levels):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    # For testing
    elif event.key == pygame.K_q:
        enemies.add(Goomba(settings, screen, 935, 270, 1))
    elif event.key == pygame.K_w:
        enemies.add(Goomba(settings, screen, 1000, 300, 2))
    elif event.key == pygame.K_e:
        enemies.add(KoopaTroopa(settings, screen, 935, 270, 1))
    elif event.key == pygame.K_r:
        enemies.add(KoopaTroopa(settings, screen, 935, 270, 2))
    elif event.key == pygame.K_t:
        enemies.add(KoopaTroopa(settings, screen, 935, 270, 3))
    elif event.key == pygame.K_y:
        enemies.add(KoopaTroopa(settings, screen, 935, 270, 4))
    elif event.key == pygame.K_u:
        enemies.add(KoopaTroopa(settings, screen, 950, 270, 5))
    elif event.key == pygame.K_i:
        enemies.add(PiranhaPlant(settings, screen, timers, 1000, 40, 1))
    elif event.key == pygame.K_o:
        enemies.add(PiranhaPlant(settings, screen, timers, 40, 400, 2))
    elif event.key == pygame.K_p:
        enemies.add(CheepCheep(settings, screen, timers, 1000, 400, 1))
    elif event.key == pygame.K_a:
        enemies.add(CheepCheep(settings, screen, timers, 1000, 400, 2))
    elif event.key == pygame.K_s:
        enemies.add(CheepCheep(settings, screen, timers, random.randint(0, 200), settings.screen_height, 3))
    elif event.key == pygame.K_d:
        enemies.add(Blooper(settings, screen, 520, 400, 1))
    elif event.key == pygame.K_f:
        enemies.add(FakeBowser(settings, screen, timers, 550, 270, 1))
    elif event.key == pygame.K_k:
        for enemy in enemies:
            enemy.take_damage()
            if enemy.ename is "piranha_plant":
                enemies.remove(enemy)
    elif event.key == pygame.K_l:
        for enemy in enemies:
            enemy.eliminate()
            if enemy.ename is "piranha_plant":
                enemies.remove(enemy)
    elif event.key == pygame.K_m:
        objects.add(Brick(settings, screen, 600, 600, 1))
    elif event.key == pygame.K_n:
        objects.add(Coin(settings, screen, 500, 600, 1))
    elif event.key == pygame.K_b:
        objects.add(Coin(settings, screen, 400, 600, 2))
    elif event.key == pygame.K_c:
        screen_x_move = 200
        screen_move(settings, enemies, objects, background, levels, screen_x_move)
    elif event.key == pygame.K_x:
        settings.move_screen = True


def check_keyup_events(event, settings, screen, timers, enemies, objects, background, levels):
    if event.key == pygame.K_x:
        settings.move_screen = False


def update_screen(screen, enemies, timers, objects, background, levels):
    if timers.curtime - timers.last_display > timers.display_wait:
        timers.last_display = timers.curtime
        for level in levels:
            if level.active:
                screen.fill(level.bg_color)
        for object in background:
            object.blitme()
        for enemy in enemies:
            enemy.blitme()
        for object in objects:
            object.blitme()
        pygame.display.flip()


def update_animations(enemies, timers, objects):
    if timers.curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        timers.last_enemy_animation = timers.curtime
        changeframe = True
        for enemy in enemies:
            enemy.update_image(changeframe)
    if timers.curtime - timers.last_object_animation > timers.object_animation_wait:
        timers.last_object_animation = timers.curtime
        for object in objects:
            object.update_image()


def update_pos(settings, timers, enemies, objects, background, levels):
    if timers.curtime - timers.last_move > timers.move_wait:
        timers.last_move = timers.curtime
        for enemy in enemies:
            enemy.update_pos(enemies, objects)
            if enemy.rect.right < -200 or enemy.rect.top > settings.screen_height + 200:
                enemies.remove(enemy)
        if settings.move_screen:
            screen_x_move = 10
            screen_move(settings, enemies, objects, background, levels, screen_x_move)


def screen_move(settings, enemies, objects, background, levels, screen_x_move):
    settings.screen_pos += screen_x_move
    for object in objects:
        object.update_pos(screen_x_move)
    for object in background:
        object.update_pos(screen_x_move)
    for enemy in enemies:
        enemy.move_with_screen(screen_x_move)
    for level in levels:
        if level.active:
            level.enemy_spawn_triggers(enemies)
