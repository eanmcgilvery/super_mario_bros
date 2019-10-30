import pygame
import sys
import random

# Import all enemies
import mario
from blooper import Blooper
from cheep_cheep import CheepCheep
from fake_bowser import FakeBowser
from goomba import Goomba
from koopa_troopa import KoopaTroopa
from piranha_plant import PiranhaPlant
from mario import Mario

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
from mushroom import Mushroom


def check_events(settings, screen, ui, timers, enemies, objects, background, levels, mario, items):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, ui, timers, enemies, objects, background, levels, mario,
                                 items)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, mario)


def check_keydown_events(event, settings, screen, ui, timers, enemies, objects, background, levels, mario, items):
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key == pygame.K_a:
        mario.idle = False
        mario.move_right = False
        mario.facing_right = False
        mario.move_left = True
    elif event.key == pygame.K_s:
        mario.crouch = True
        mario.move_right = False
        mario.move_left = False
    elif event.key == pygame.K_d:
        mario.idle = False
        mario.move_right = True
        mario.facing_right = True
        mario.move_left = False

    elif event.key == pygame.K_c:
        mario.crouch = True
        mario.idle = False
        mario.move_left = False
        mario.move_right = False
        mario.jump_ = False

    if event.key == pygame.K_SPACE:
        mario.idle = False
        mario.jump_ = True
        mario.allow_jump = True
        mario.crouch = False

    if event.key == pygame.K_v:
        mario.run = True


def check_keyup_events(event, settings, mario_):
    if event.key == pygame.K_x:
        settings.move_screen = False
    if event.key == pygame.K_d:
        mario_.idle = True
        mario_.move_right = False
    if event.key == pygame.K_a:
        mario_.move_left = False
    if event.key == pygame.K_s:
        mario_.idle = True
        mario_.crouch = False
    if event.key == pygame.K_SPACE:
        mario_.idle = True
        mario_.jump_ = False
    if event.key == pygame.K_v:
        mario_.run = False
    if event.key == pygame.K_c:
        mario.crouch = False

def update_screen(screen, ui, enemies, timers, objects, background, levels, mario, items, menu):
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
        ui.blitme()
        for object in items:
            object.blitme()
        mario.blitme()

        pygame.display.flip()


def update_animations(enemies, timers, objects, mario, settings, items):
    if timers.curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        timers.last_enemy_animation = timers.curtime
        changeframe = True

        mario.animation(timers.curtime % 3)

        for enemy in enemies:
            enemy.update_image(changeframe)
    if timers.curtime - timers.last_object_animation > timers.object_animation_wait:
        timers.last_object_animation = timers.curtime
        for object in objects:
            object.update_image()
    for enemy in enemies:
        if enemy.ename is "goomba" and enemy.is_dead and not enemy.eliminated:
            if timers.curtime - enemy.moment_of_death > timers.goomba_death_wait:
                enemies.remove(enemy)
        if enemy.ename is "koopa_troopa" and enemy.is_dead and not enemy.eliminated:
            enemy.reanimate()


def update_pos(settings, timers, enemies, objects, background, levels, items, mario):
    if timers.curtime - timers.last_move > timers.move_wait:
        timers.last_move = timers.curtime
        for enemy in enemies:
            enemy.update_pos(enemies, objects)
            if enemy.rect.right < -200 or enemy.rect.top > settings.screen_height + 200:
                enemies.remove(enemy)
        for object in items:
            object.update_pos(enemies, objects)
        mario.update_pos(enemies, objects, settings)
        if mario.x >= settings.screen_width / 2 and mario.move_right:
            if not mario.run:
                screen_x_move = settings.WALK_SPEED
            else:
                screen_x_move = settings.RUN_SPEED
            screen_move(settings, enemies, objects, background, levels, screen_x_move)
            mario.move_with_screen(screen_x_move)


def update_level_timer(ui, timers, mario):
    if timers.curtime - timers.last_game_countdown > timers.game_countdown_wait:
        timers.last_game_countdown = timers.curtime
        if ui.time <= 0:
            mario.death()
            pass
        else:
            ui.time -= 1


def screen_move(settings, enemies, objects, background, levels, screen_x_move):
    settings.screen_pos += screen_x_move
    for object in objects:
        object.move_with_screen(screen_x_move)
    for object in background:
        object.move_with_screen(screen_x_move)
    for enemy in enemies:
        enemy.move_with_screen(screen_x_move)
    for level in levels:
        if level.active:
            level.enemy_spawn_triggers(enemies)
