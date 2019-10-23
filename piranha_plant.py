import pygame
from enemy import Enemy


class PiranhaPlant(Enemy):
    def __init__(self, settings, screen, timers, x, y, etype):
        super(PiranhaPlant, self).__init__(settings, screen, x, y, etype)
        self.timers = timers

        self.speed = self.settings.piranha_plant_speed
        self.move_destination = y - settings.piranha_plant_height
        self.last_move = self.timers.curtime
        self.last_direction_was_up = True

        """etype 1 is green piranha plant, 2 is blue"""
        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.piranha_plant_width, settings.piranha_plant_height)
        if etype is 1:
            self.pic = pygame.image.load('images/Piranha_Plant1a1.png')
        elif etype is 2:
            self.pic = pygame.image.load('images/Piranha_Plant2a1.png')
        self.image = pygame.transform.scale(self.pic, (settings.piranha_plant_width, settings.piranha_plant_height))

    def update_pos(self):
        if self.last_direction_was_up:
            if self.timers.curtime - self.last_move > self.timers.piranha_plant_pipe_wait:
                self.update_pos_helper()
        elif not self.last_direction_was_up:
            if self.timers.curtime - self.last_move > self.timers.piranha_plant_move_wait:
                self.update_pos_helper()

    def update_pos_helper(self):
        self.y += self.speed
        if self.last_direction_was_up and self.y < self.move_destination or not self.last_direction_was_up and self.y > self.move_destination:
            self.y = self.move_destination
            self.last_move = self.timers.curtime
            if self.last_direction_was_up:  # Last moved upwards
                self.move_destination = self.y + self.settings.piranha_plant_height
                self.last_direction_was_up = False
            else:
                self.move_destination = self.y - self.settings.piranha_plant_height
                self.last_direction_was_up = True
            self.speed = self.speed * -1
        self.rect.y = self.y

    def update_image(self):
        # Alternate normal alive animation
        if self.frame is 1:
            if self.etype is 1:
                self.pic = pygame.image.load('images/Piranha_Plant1a2.png')
            elif self.etype is 2:
                self.pic = pygame.image.load('images/Piranha_Plant2a2.png')
            self.frame = 2
        elif self.frame is 2:
            if self.etype is 1:
                self.pic = pygame.image.load('images/Piranha_Plant1a1.png')
            elif self.etype is 2:
                self.pic = pygame.image.load('images/Piranha_Plant2a1.png')
            self.frame = 1
        self.image = pygame.transform.scale(self.pic, (self.settings.piranha_plant_width, self.settings.piranha_plant_height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
