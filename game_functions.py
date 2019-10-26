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


def check_events(settings, screen, timers, enemies, objects, background):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, screen, timers, enemies, objects, background)


def check_keydown_events(event, settings, screen, timers, enemies, objects, background):
    # For testing
    if event.key == pygame.K_q:
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
    elif event.key == pygame.K_m:
        objects.add(Brick(settings, screen, 600, 600, 1))
    elif event.key == pygame.K_n:
        objects.add(Coin(settings, screen, 500, 600, 1))
    elif event.key == pygame.K_b:
        objects.add(Coin(settings, screen, 400, 600, 2))
    elif event.key == pygame.K_c:
        for object in objects:
            object.update_pos()
        for object in background:
            object.update_pos()


def update_screen(screen, enemies, timers, objects, background):
    if timers.curtime - timers.last_display > timers.display_wait:
        timers.last_display = timers.curtime
        # Level 1-1 Background color
        screen.fill((170, 170, 255))
        for object in objects:
            object.blitme()
        for object in background:
            object.blitme()
        for enemy in enemies:
            enemy.blitme()
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




def update_pos(settings, timers, enemies, objects):
    if timers.curtime - timers.last_move > timers.move_wait:
        timers.last_move = timers.curtime
        for enemy in enemies:
            enemy.update_pos(enemies, objects)
            if enemy.rect.right < -200 or enemy.rect.top > settings.screen_height + 200:
                enemies.remove(enemy)
    if timers.curtime - timers.last_move > timers.move_wait:
        timers.last_move = timers.curtime
        for object in objects:
            object.update_pos()




def generate_ground_for_1_1(settings, screen, objects):
    for x in range(69):
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))


def generate_map_1_1(settings, screen, objects, background):

    generate_ground_for_1_1(settings, screen, objects)

    background.add(Hill(settings, screen, 0, settings.ground_level - settings.large_hill_height, 2))
    background.add(Cloud(settings, screen, settings.brick_lenth * 9, settings.brick_lenth * 3, 1))
    background.add(Bush(settings, screen, settings.brick_lenth * 12, settings.ground_level - settings.brick_lenth, 3))
    background.add(Hill(settings, screen, settings.brick_lenth * 16, settings.ground_level - settings.brick_lenth - 2, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 16, settings.ground_level - settings.brick_lenth * 4, 1))
    background.add(Cloud(settings, screen, settings.brick_lenth * 20, settings.ground_level - settings.brick_lenth * 15, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 22, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 20, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 21, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 22, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 23, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 24, settings.ground_level - settings.brick_lenth * 4, 3))
    background.add(Bush(settings, screen, settings.brick_lenth *23.5, settings.ground_level - settings.brick_lenth, 1))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 29, settings.ground_level - settings.brick_lenth * 2, 1))

#def redrawWindow(screen, map, bgx, bgx2):
 #   screen.blit(bg, (bgx, 0))
  #  screen.blit(bg, (bgx2, 0))
   # pygame.display.update()
