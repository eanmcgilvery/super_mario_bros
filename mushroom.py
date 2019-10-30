import pygame
from object import Object


class Mushroom(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Mushroom, self).__init__(settings, screen, x, y, otype)

        self.width = settings.goomba_width
        self.height = settings.goomba_height
        self.name = "mushroom"
        self.pic = pygame.image.load('images/mushroom.png')
        self.rect = pygame.Rect(x, y, settings.mushroom_width, settings.mushroom_height)
        self.image = pygame.transform.scale(self.pic, (settings.mushroom_width, settings.mushroom_height))

    def update_image(self):
        self.image = self.image

    def update_pos(self, enemies, objects):

        self.x += self.settings.goomba_speed * self.x_direction
        self.y_velocity += self.settings.fall_acceleration
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
        self.check_collisions(objects)

    def check_collisions(self, objects):
        if not self.eliminated:
            for object in objects:
                if self.rect.colliderect(object):
                    if self.rect.bottom > object.rect.top and self.y_velocity >= self.rect.bottom - object.rect.top:  # Reposition goomba to the top of the object
                        self.y = object.rect.top - self.height
                        self.y_velocity = 0
                    elif object.rect.bottom > self.rect.top and self.y_velocity * -1 >= object.rect.bottom - self.rect.top:  # Reposition to the bottom
                        self.y = object.rect.bottom
                        self.y_velocity = 0
                    elif self.rect.right - object.rect.left < object.rect.right - self.rect.left:  # Reposition to the left
                        if self.x_direction is 1:  # When not moving left change direction to the left
                            self.x = object.rect.left - self.width
                            self.x_direction = -1
                    else:  # Reposition to the right
                        if self.x_direction is -1:  # When not moving right change direction to the right
                            self.x = object.rect.right
                            self.x_direction = 1
                    self.rect.x = self.x
                    self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
