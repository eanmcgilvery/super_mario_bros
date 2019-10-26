class Settings:
    def __init__(self):
        """FEEL FREE TO CHANGE SCREEN WIDTH AND SCREEN HEIGHT"""
        # Screen settings
        self.map_width = 5000
        self.map_height = 700

        self.screen_width = 1200
        self.screen_height = 700

        self.ground_level = self.map_height - 50

        # Mario Speed
        self.MAX_WALKING_SPEED = 10
        self.MAX_HEIGHT_SPEED = 5

        # Speed of gravity in our world
        self.MAX_FALL_SPEED = 9.8

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
        self.blooper_speed = self.goomba_speed * 2
        self.fake_bowser_speed = self.goomba_speed

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

        self.small_hill_width = self.brick_lenth * 3
        self.small_hill_height = self.brick_lenth + 3
        self.large_hill_width = self.brick_lenth * 5
        self.large_hill_height = self.brick_lenth * 2

        self.small_bush_width = self.brick_lenth * 2
        self.small_bush_height =self.brick_lenth
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