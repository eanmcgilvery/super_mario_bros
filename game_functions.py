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


def check_events(settings, screen, timers, enemies, objects, background, levels, mario, items):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, timers, enemies, objects, background, levels, mario, items)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, screen, timers, enemies, objects, background, levels)


def check_keydown_events(event, settings, screen, timers, enemies, objects, background, levels, mario, items):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    # For testing
    elif event.key == pygame.K_q:
        enemies.add(Goomba(settings, screen, timers, 935, 270, 1))
    elif event.key == pygame.K_w:
        enemies.add(Goomba(settings, screen, timers, 1000, 300, 2))
    elif event.key == pygame.K_e:
        enemies.add(KoopaTroopa(settings, screen, timers, 935, 270, 1))
    elif event.key == pygame.K_r:
        enemies.add(KoopaTroopa(settings, screen, timers, 935, 270, 2))
    elif event.key == pygame.K_t:
        enemies.add(KoopaTroopa(settings, screen, timers, 935, 270, 3))
    elif event.key == pygame.K_y:
        enemies.add(KoopaTroopa(settings, screen, timers, 935, 270, 4))
    elif event.key == pygame.K_u:
        enemies.add(KoopaTroopa(settings, screen, timers, 950, 270, 5))
    elif event.key == pygame.K_i:
        enemies.add(PiranhaPlant(settings, screen, timers, 1000, 40, 1))
    elif event.key == pygame.K_o:
        enemies.add(PiranhaPlant(settings, screen, timers, 40, 400, 2))
    elif event.key == pygame.K_p:
        enemies.add(CheepCheep(settings, screen, timers, 1000, 400, 1))
    elif event.key == pygame.K_a:
        enemies.add(CheepCheep(settings, screen, timers, 1000, 400, 2))
        mario.walk(settings)
    elif event.key == pygame.K_s:
        enemies.add(CheepCheep(settings, screen, timers, random.randint(0, 200), settings.screen_height, 3))
    elif event.key == pygame.K_d:
        enemies.add(Blooper(settings, screen, timers, 520, 400, 1))
        mario.walk(settings)
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
        items.add(Mushroom(settings, screen, 300, 600, 2))
    elif event.key == pygame.K_c:
        screen_x_move = 200
        screen_move(settings, enemies, objects, background, levels, screen_x_move)
    elif event.key == pygame.K_x:
        settings.move_screen = True


def check_keyup_events(event, settings, screen, timers, enemies, objects, background, levels):
    if event.key == pygame.K_x:
        settings.move_screen = False


def update_screen(screen, enemies, timers, objects, background, levels, mario, items):
def update_screen(screen, ui, enemies, timers, objects, background, levels, mario):
    if timers.curtime - timers.last_display > timers.display_wait:
        timers.last_display = timers.curtime

        mario.blitme()
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
        pygame.display.flip()


def update_animations(enemies, timers, objects, mario, settings, items):

    mario.walk(settings)

    if timers.curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        timers.last_enemy_animation = timers.curtime
        changeframe = True
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


def update_pos(settings, timers, enemies, objects, background, levels, items):
    if timers.curtime - timers.last_move > timers.move_wait:
        timers.last_move = timers.curtime
        for enemy in enemies:
            enemy.update_pos(enemies, objects)
            if enemy.rect.right < -200 or enemy.rect.top > settings.screen_height + 200:
                enemies.remove(enemy)
        for object in items:
            object.update_pos(enemies,objects)
        if settings.move_screen:
            screen_x_move = 10
            screen_move(settings, enemies, objects, background, levels, screen_x_move)


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

def check_keydown(event, mario):
    if event.key == pygame.K_d:
        mario.facing_right = True
    elif event.key == pygame.K_a:
        mario.facing_right = False
    if event.key == pygame.K_SPACE:
        mario.jump()