import random
import pygame

class Timers:
    """Timers used for animations, movement, screen display, etc"""
    def __init__(self):
        # Update one timer per loop to base everything else on
        self.curtime = 0

        # Display refresh rate
        self.last_display = 0
        self.display_wait = 30

        # Game timer counting down one second at a time
        self.last_game_countdown = 0
        self.game_countdown_wait = 1000

        # Enemies animate together
        self.last_enemy_animation = 0
        self.enemy_animation_wait = 500

        self.last_object_animation = 0
        self.object_animation_wait = 500

        # General movement
        self.last_move = 0
        self.move_wait = 30

        # Goomba squish animation time
        self.goomba_death_wait = 1000

        # Koopa returning back to life animation
        self.koopa_reanimate_wait = 5000
        self.koopa_come_back_wait = self.koopa_reanimate_wait + 2000
        self.koopa_legs_wait = 250

        # Koopa kick invincibility
        self.last_shell_kick = 0
        self.shell_kick_wait = 250

        # Cheep cheep move animations
        self.cheep_y_change_wait = 5000

        # Piranha Plant animations
        self.piranha_plant_move_wait = 1500
        self.piranha_plant_pipe_wait = 3000

        # Bowser move, jump, and flame frequency
        self.fake_bowser_move_wait = random.randint(2000, 4000)  # Needs to be reset every time it is used
        self.fake_bowser_next_move_wait = self.fake_bowser_move_wait + random.randint(1000, 3000)
        self.fake_bowser_jump_wait = random.randint(5000, 10000)  # Needs to be reset every time it is used


