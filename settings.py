import pygame

class Settings:
    def __init__(self):
        """FEEL FREE TO CHANGE SCREEN WIDTH AND SCREEN HEIGHT"""
        # Screen settings
        self.map_width = 5000
        self.map_height = 700

        self.screen_width = 1200
        self.screen_height = 700

        self.screen_pos = 0
        self.ground_level = self.map_height - 50

        # Fall acceleration
        self.fall_acceleration = 1
        self.swimming_fall_acceleration = 0.5

        # All enemy sizes depend on screen height
        self.goomba_width = int(self.screen_height / 17.5)
        self.goomba_height = self.goomba_width

        self.koopa_width = self.goomba_width
        self.koopa_height = int(self.goomba_height * 1.5)

        self.dead_koopa_width = self.goomba_width
        self.dead_koopa_height = self.goomba_height

        self.piranha_plant_width = self.koopa_width
        self.piranha_plant_height = self.koopa_height

        self.cheep_width = self.goomba_width
        self.cheep_height = self.goomba_height

        self.blooper_width = self.koopa_width
        self.bloopera1_height = self.koopa_height
        self.bloopera2_height = self.goomba_height

        self.fake_bowser_width = self.goomba_width * 2
        self.fake_bowser_height = self.goomba_height * 2

        self.bowser_fire_width = int(self.goomba_width * 1.5)
        self.bowser_fire_height = int(self.goomba_height * 0.5)

        # Enemy speeds
        self.goomba_speed = 2.5
        self.koopa_speed = self.goomba_speed
        self.piranha_plant_speed = self.koopa_speed / 2 * -1
        self.cheep_speed = self.goomba_speed
        self.cheep_y_speed = 0.5
        self.blooper_speed = self.goomba_speed * 2
        self.fake_bowser_speed = self.goomba_speed * 1.5

        self.enemy_jump_speed = -18

        # Fake Bowser leash range (He has to stay put in a certain area but still move)
        self.fake_bowser_leash = [0, 250]
        self.fake_bowser_pos = self.fake_bowser_leash[1] / 2  # Starts in the center of the leash range

        # All bricks size depends on screen height
        self.brick_lenth = self.goomba_width

        # Object size depends on bricksize
        self.small_cloud_width = self.brick_lenth * 2
        self.small_cloud_height = self.brick_lenth * 2
        self.medium_cloud_width = self.brick_lenth * 3
        self.medium_cloud_height = self.brick_lenth * 2
        self.large_cloud_width = self.brick_lenth * 4
        self.large_cloud_height = self.brick_lenth * 2

        self.small_pipe_width = self.brick_lenth * 2
        self.small_pipe_height = self.brick_lenth * 2
        self.medium_pipe_width = self.brick_lenth * 2
        self.medium_pipe_height = self.brick_lenth * 3
        self.large_pipe_width = self.brick_lenth * 2
        self.large_pipe_height = self.brick_lenth * 4
        self.pipe1_1_width = self.brick_lenth * 2
        self.pipe1_1_height = self.brick_lenth * 2
        self.pipe1_2_width = self.brick_lenth * 2
        self.pipe1_2_height = self.brick_lenth * 2
        self.pipe1_3_width = self.brick_lenth * 2
        self.pipe1_3_height = self.brick_lenth

        self.small_hill_width = self.brick_lenth * 3
        self.small_hill_height = self.brick_lenth + 3
        self.large_hill_width = self.brick_lenth * 5
        self.large_hill_height = self.brick_lenth * 2

        self.small_bush_width = self.brick_lenth * 2
        self.small_bush_height = self.brick_lenth
        self.medium_bush_width = self.brick_lenth * 3
        self.medium_bush_height = self.brick_lenth
        self.large_bush_height = self.brick_lenth
        self.large_bush_width = self.brick_lenth * 4

        self.flag_pole_width = self.brick_lenth
        self.flag_pole_height = self.brick_lenth * 11.5

        self.small_castle_width = self.brick_lenth * 5
        self.small_castle_height = self.brick_lenth * 5
        self.castle_flag_width = self.brick_lenth
        self.castle_flag_height = self.brick_lenth

        self.coin_width = self.brick_lenth
        self.coin_height = self.brick_lenth
        self.spin_coin_width = self.brick_lenth / 5
        self.spin_coin_height = self.brick_lenth

        self.ground_level = self.map_height - self.brick_lenth * 1.5

        # Items
        self.mushroom_width = self.brick_lenth
        self.mushroom_height = self.brick_lenth
        self.star_width = self.brick_lenth
        self.star_height = self.brick_lenth
        self.flower_width = self.brick_lenth
        self.flower_height = self.brick_lenth

        # Music
        self.background_sound = pygame.mixer.Sound('sounds/main_theme.ogg')
        self.underground_sound = pygame.mixer.Sound('sounds/underground.wav')

        # FOR TESTING
        self.move_screen = False

        # Mario Settings
        self.mario_small_width = self.goomba_width
        self.mario_small_height = self.goomba_height

        # MARIO FORCES
        self.WALK_SPEED = 8
        self.RUN_ACCEL = 20
        self.SMALL_TURNAROUND = .35

        self.GRAVITY = 1.01
        self.JUMP_GRAVITY = .31
        self.JUMP_VEL = 10
        self.FAST_JUMP_VEL = -12.5
        self.MAX_Y_VEL = 11

        self.MAX_RUN_SPEED = 800
        self.MAX_WALK_SPEED = 6

        # Mario States
        self.STAND = 'standing'
        self.WALK = 'walk'
        self.JUMP = 'jump'
        self.FALL = 'fall'
        self.SMALL_TO_BIG = 'small to big'
        self.BIG_TO_FIRE = 'big to fire'
        self.BIG_TO_SMALL = 'big to small'
        self.FLAGPOLE = 'flag pole'
        self.WALKING_TO_CASTLE = 'walking to castle'
        self.END_OF_LEVEL_FALL = 'end of level fall'

        # Speed of gravity in our world
        self.FALL_SPEED = -9.8
