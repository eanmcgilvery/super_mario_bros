import pygame


def update_animations(timers):
    curtime = pygame.time.get_ticks()
    if curtime - timers.last_enemy_animation > timers.enemy_animation_wait:
        '''enemies.update_image()'''
