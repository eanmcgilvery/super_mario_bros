import pygame
import sys
import mario
import math


def check_events(settings, mario_):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mario_)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, settings, mario_)


def check_keydown_events(event, mario_, ):
    if event.key == pygame.K_ESCAPE:
        sys.exit()

    elif event.key == pygame.K_a:
        mario_.idle = False
        mario_.move_right = False
        mario_.facing_right = False
        mario_.move_left = True
    elif event.key == pygame.K_s:
        mario_.crouch = True
        mario_.move_right = False
        mario_.move_left = False
        mario_.jump_ = False

    elif event.key == pygame.K_d:
        mario_.idle = False
        mario_.move_right = True
        mario_.facing_right = True
        mario_.move_left = False

    if event.key == pygame.K_SPACE:
        pygame.mixer.Sound('sounds/small_jump.ogg').play()
        mario_.idle = False
        mario_.jump_ = True
        mario_.allow_jump = True
        mario_.crouch = False

    if event.key == pygame.K_v:
        mario_.run = True


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


def update_screen(screen, ui, enemies, timers, objects, background, levels, mario_, items):
    if timers.curtime - timers.last_display > timers.display_wait:
        timers.last_display = timers.curtime

        for level in levels:
            if level.active:
                screen.fill(level.bg_color)
        for object_ in background:
            object_.blitme()
        for enemy in enemies:
            enemy.blitme()

        for object_ in objects:
            object_.blitme()
        ui.blitme()
        for object_ in items:
            object_.blitme()

        mario_.blitme()

        pygame.display.flip()


def update_animations(enemies, timers, objects, mario_):
    if timers.curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        timers.last_enemy_animation = timers.curtime
        changeframe = True

        for enemy in enemies:
            enemy.update_image(changeframe)

    if mario_.index >= 3:
        mario_.index = 0
    else:
        mario_.index += 1

    mario_.animation(mario_.index - 1)

    if timers.curtime - timers.last_object_animation > timers.object_animation_wait:
        timers.last_object_animation = timers.curtime
        for object_ in objects:
            object_.update_image()
    for enemy in enemies:
        if enemy.ename is "goomba" and enemy.is_dead and not enemy.eliminated:
            if timers.curtime - enemy.moment_of_death > timers.goomba_death_wait:
                enemies.remove(enemy)
        if enemy.ename is "koopa_troopa" and enemy.is_dead and not enemy.eliminated:
            enemy.reanimate()


def update_pos(settings, timers, enemies, objects, background, levels, items, mario_, ui):
    if timers.curtime - timers.last_move > timers.move_wait:
        timers.last_move = timers.curtime
        for enemy in enemies:
            enemy.update_pos(enemies, objects)
            if enemy.rect.right < -200 or enemy.rect.top > settings.screen_height + 200:
                enemies.remove(enemy)
        for object_ in items:
            object_.update_pos(enemies, objects)

        # Move camera with Mario
        mario_.update_pos(enemies, objects, settings, ui)
        if mario_.x >= settings.screen_width / 2 and mario_.move_right:
            if not mario_.run:
                screen_x_move = settings.WALK_SPEED
            else:
                screen_x_move = settings.RUN_SPEED
            screen_move(settings, enemies, objects, background, levels, screen_x_move)
            mario_.move_with_screen(screen_x_move)


def update_level_timer(ui, timers, mario_):
    if timers.curtime - timers.last_game_countdown > timers.game_countdown_wait:
        timers.last_game_countdown = timers.curtime
        if ui.time <= 0:
            mario_.death()
            pass
        else:
            ui.time -= 1


def screen_move(settings, enemies, objects, background, levels, screen_x_move):
    settings.screen_pos += screen_x_move
    for object_ in objects:
        object_.move_with_screen(screen_x_move)
    for object_ in background:
        object_.move_with_screen(screen_x_move)
    for enemy in enemies:
        enemy.move_with_screen(screen_x_move)
    for level in levels:
        if level.active:
            level.enemy_spawn_triggers(enemies)
