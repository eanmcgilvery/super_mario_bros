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
        screen_move(enemies, objects, background, 200)


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


def screen_move(enemies, objects, background, screen_x_move):
    for object in objects:
        object.update_pos(screen_x_move)
    for object in background:
        object.update_pos(screen_x_move)
    for enemy in enemies:
        enemy.move_with_screen(screen_x_move)


def generate_ground_for_1_1(settings, screen, objects):
    for x in range(70):
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))
    for x in range(72,87):
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))
    for x in range(90, 154):
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level, 2))
        objects.add(Brick(settings, screen, settings.brick_lenth * x, settings.ground_level + settings.brick_lenth, 2))
    for x in range(156,213):
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
    objects.add(Pipe(settings, screen, settings.brick_lenth * 39, settings.ground_level - settings.brick_lenth * 3, 2))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 47, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 58, settings.ground_level - settings.brick_lenth * 4, 3))
    background.add(Cloud(settings, screen, settings.brick_lenth * 28, settings.ground_level - settings.brick_lenth * 12, 3))
    background.add(Cloud(settings, screen, settings.brick_lenth * 37, settings.ground_level - settings.brick_lenth * 15, 2))
    background.add(Bush(settings, screen, settings.brick_lenth * 41.5, settings.ground_level - settings.brick_lenth, 3))
    background.add(Hill(settings, screen, settings.brick_lenth * 49, settings.ground_level - settings.large_hill_height - 2, 2))
    background.add(Cloud(settings, screen, settings.brick_lenth * 57, settings.ground_level - settings.brick_lenth * 15, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 65, settings.ground_level - settings.brick_lenth * 5, 1))
    background.add(Bush(settings, screen, settings.brick_lenth * 60.5, settings.ground_level - settings.brick_lenth, 3))
    background.add(Hill(settings, screen, settings.brick_lenth * 65, settings.ground_level - settings.small_hill_height, 1))
    background.add(Cloud(settings, screen, settings.brick_lenth * 68, settings.ground_level - settings.brick_lenth * 15, 1))
    background.add(Bush(settings, screen, settings.brick_lenth * 72.5, settings.ground_level - settings.brick_lenth, 1))
    background.add(Cloud(settings, screen, settings.brick_lenth * 76, settings.ground_level - settings.brick_lenth * 13, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 78, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 79, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 80, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 81, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 82, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 83, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 84, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 85, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 86, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 87, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 88, settings.ground_level - settings.brick_lenth * 8, 3))
    background.add(Cloud(settings, screen, settings.brick_lenth * 85, settings.ground_level - settings.brick_lenth * 15, 2))
    objects.add(Brick(settings, screen, settings.brick_lenth * 92, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 93, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 94, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 95, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 95, settings.ground_level - settings.brick_lenth * 4, 3))
    background.add(Bush(settings, screen, settings.brick_lenth * 90.5, settings.ground_level - settings.brick_lenth, 2))
    background.add(Hill(settings, screen, settings.brick_lenth * 97, settings.ground_level - settings.large_hill_height - 2, 2))
    objects.add(Brick(settings, screen, settings.brick_lenth * 101, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 102, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 107, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 110, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 113, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 110, settings.ground_level - settings.brick_lenth * 8, 1))
    background.add(Cloud(settings, screen, settings.brick_lenth * 106, settings.ground_level - settings.brick_lenth * 11, 1))
    background.add(Bush(settings, screen, settings.brick_lenth * 108.5, settings.ground_level - settings.brick_lenth, 3))
    background.add(Hill(settings, screen, settings.brick_lenth * 113, settings.ground_level - settings.small_hill_height, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 119, settings.ground_level - settings.brick_lenth * 4, 3))
    background.add(Cloud(settings, screen, settings.brick_lenth * 116, settings.ground_level - settings.brick_lenth * 12, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 122, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 123, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 124, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 129, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 130, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 131, settings.ground_level - settings.brick_lenth * 8, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 132, settings.ground_level - settings.brick_lenth * 8, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 130, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 131, settings.ground_level - settings.brick_lenth * 4, 3))
    background.add(Bush(settings, screen, settings.brick_lenth * 120.5, settings.ground_level - settings.brick_lenth, 1))
    background.add(Cloud(settings, screen, settings.brick_lenth * 124, settings.ground_level - settings.brick_lenth * 11, 3))
    background.add(Cloud(settings, screen, settings.brick_lenth * 133, settings.ground_level - settings.brick_lenth * 13, 2))
    background.add(Bush(settings, screen, settings.brick_lenth * 138.5, settings.ground_level - settings.brick_lenth, 2))
    background.add(Hill(settings, screen, settings.brick_lenth * 145, settings.ground_level - settings.large_hill_height, 2))
    background.add(Cloud(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 11, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 135, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 136, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 137, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 136, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 137, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 137, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 138, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 141, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 142, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 142, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 142, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 143, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 143, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 144, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 149, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 150, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 150, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 151, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 151, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 151, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 152, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 153, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 156, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 157, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 157, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 157, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 158, settings.ground_level - settings.brick_lenth * 1, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 158, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 159, settings.ground_level - settings.brick_lenth * 1, 4))
    background.add(Hill(settings, screen, settings.brick_lenth * 161, settings.ground_level - settings.small_hill_height, 1))
    background.add(Cloud(settings, screen, settings.brick_lenth * 164, settings.ground_level - settings.brick_lenth * 13, 1))
    background.add(Cloud(settings, screen, settings.brick_lenth * 172, settings.ground_level - settings.brick_lenth * 11, 3))
    background.add(Cloud(settings, screen, settings.brick_lenth * 181, settings.ground_level - settings.brick_lenth * 13, 2))
    background.add(Cloud(settings, screen, settings.brick_lenth * 201, settings.ground_level - settings.brick_lenth * 11, 1))
    background.add(Bush(settings, screen, settings.brick_lenth * 167.5, settings.ground_level - settings.brick_lenth, 1))
    background.add(Hill(settings, screen, settings.brick_lenth * 193, settings.ground_level - settings.large_hill_height, 2))
    background.add(Hill(settings, screen, settings.brick_lenth * 209, settings.ground_level - settings.small_hill_height, 1))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 164, settings.ground_level - settings.brick_lenth * 2, 1))
    objects.add(Pipe(settings, screen, settings.brick_lenth * 180, settings.ground_level - settings.brick_lenth * 2, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 169, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 170, settings.ground_level - settings.brick_lenth * 4, 3))
    objects.add(Brick(settings, screen, settings.brick_lenth * 171, settings.ground_level - settings.brick_lenth * 4, 1))
    objects.add(Brick(settings, screen, settings.brick_lenth * 172, settings.ground_level - settings.brick_lenth * 4, 3))

    objects.add(Brick(settings, screen, settings.brick_lenth * 182, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 183, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 183, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 184, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 184, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 184, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 185, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 186, settings.ground_level - settings.brick_lenth * 5, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 5, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 187, settings.ground_level - settings.brick_lenth * 6, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 5, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 6, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 188, settings.ground_level - settings.brick_lenth * 7, 4))

    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 5, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 6, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 7, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 189, settings.ground_level - settings.brick_lenth * 8, 4))

    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 2, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 3, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 4, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 5, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 6, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 7, 4))
    objects.add(Brick(settings, screen, settings.brick_lenth * 190, settings.ground_level - settings.brick_lenth * 8, 4))


    objects.add(Flag_Pole(settings, screen, settings.brick_lenth * 199, settings.ground_level - settings.flag_pole_height, 1))
    objects.add(Castle(settings, screen, settings.brick_lenth * 203, settings.ground_level - settings.small_castle_height, 1))