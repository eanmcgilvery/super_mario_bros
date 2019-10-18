class Settings:
    def __init__(self):
        """ALL NUMBERS ARE JUST PLACEHOLDERS, FEEL FREE TO CHANGE SCREEN WIDTH AND SCREEN HEIGHT"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700

        # Mario Speed
        self.MAX_WALKING_SPEED = 10
        self.MAX_HEIGHT_SPEED = 5

        # Speed of gravity in our world
        self.MAX_FALL_SPEED = 9.8

        # Enemy sizes
        self.goomba_width = 35
        self.goomba_height = 35

        self.koopa_width = self.goomba_width
        self.koopa_height = self.goomba_height

        self.piranha_plant_width = self.koopa_width
        self.piranha_plant_height = self.piranha_plant_width * 2

        self.cheep_width = self.goomba_width
        self.cheep_height = self.goomba_height

        self.blooper_width = self.koopa_width
        self.blooper_height = self.koopa_height

        self.fake_bowser_width = self.koopa_width * 1.5
        self.fake_bowser_height = self.koopa_height * 2

        # Enemy speeds
        self.goomba_speed = 1.0
        self.koopa_speed = self.goomba_speed
        self.piranha_plant_speed = self.koopa_speed / 2
        self.cheep_speed = self.goomba_speed
        self.blooper_speed = self.goomba_speed * 2
        self.fake_bowser_speed = self.goomba_speed
