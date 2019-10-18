import pygame
from enemy import Enemy


class PiranhaPlant(Enemy):
    def __init__(self, settings, screen, x, y):
        super(PiranhaPlant, self).__init__(settings, screen, x, y)

        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.piranha_plant_width, settings.piranha_plant_height)
        self.pic = pygame.image.load('images/Piranha_Plant1.png')
        self.image = pygame.transform.scale(self.pic, (settings.piranha_plant_width, settings.piranha_plant_height))
