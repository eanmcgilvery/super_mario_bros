class Settings:
    def __init__(self):
        """ALL NUMBERS ARE JUST PLACEHOLDERS, FEEL FREE TO CHANGE SCREEN WIDTH AND SCREEN HEIGHT"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700

        # Enemy sizes
        self.goomba_width = 35
        self.goomba_height = 35
        self.koopa_width = self.goomba_width
        self.koopa_height = self.goomba_height
        self.hammer_bro_width = self.koopa_width
        self.hammer_bro_height = self.koopa_height
        self.lakitu_width = self.koopa_width
        self.lakitu_height = self.koopa_height
        self.piranha_plant_width = self.koopa_width
        self.piranha_plant_height = self.piranha_plant_width * 3
        self.spiny_width = self.goomba_width
        self.spiny_height = self.goomba_height
        self.cheep_width = self.goomba_width
        self.cheep_height = self.goomba_height
        self.blooper_width = self.koopa_width
        self.blooper_height = self.koopa_height
        self.bullet_bill_width = self.goomba_width
        self.bullet_bill_height = self.goomba_height
        self.buzzy_width = self.spiny_width
        self.buzzy_height = self.spiny_height

        # Enemy speeds
        self.enemy_fall_speed_min = 1
        self.enemy_fall_speed_inc = 1.5
        self.enemy_fall_speed_max = 4
        self.goomba_speed = 1
        self.koopa_speed = self.goomba_speed
        self.hammer_bro_speed = self.koopa_speed / 2
        self.lakitu_speed = self.koopa_speed * 2
        self.piranha_plant_speed = self.koopa_speed / 2
        self.spiny_speed = self.goomba_speed
        self.cheep_speed = self.goomba_speed
        self.blooper_speed = self.goomba_speed * 2
        self.bullet_bill_speed = self.goomba_speed
        self.buzzy_speed = self.spiny_speed
