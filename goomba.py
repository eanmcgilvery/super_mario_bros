import pygame
from enemy import Enemy


class Goomba(Enemy):
    def __init__(self, settings, screen, ui, timers,  x, y, etype):
        super(Goomba, self).__init__(settings, screen, ui, timers, x, y, etype, ename="goomba")

        self.width = settings.goomba_width
        self.height = settings.goomba_height
        self.moment_of_death = 0

        """etype 1 is brown goomba, 2 is blue goomba"""
        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, self.width, self.height)
        if etype is 1:
            self.pic = pygame.image.load('images/Goomba1a1.png')
        elif etype is 2:
            self.pic = pygame.image.load('images/Goomba2a1.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def update_pos(self, enemies, objects):
        if not self.is_dead and not self.eliminated:
            self.x += self.settings.goomba_speed * self.x_direction
        self.y_velocity += self.settings.fall_acceleration
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
        self.check_collisions(enemies, objects)

    def update_image(self, changeframe):
        # Alternate normal alive animation
        if not self.is_dead and not self.eliminated:
            if self.frame is 1 and self.etype is 1:
                self.frame = 2
                self.pic = pygame.image.load('images/Goomba1a2.png')
            elif self.frame is 2 and self.etype is 1:
                self.frame = 1
                self.pic = pygame.image.load('images/Goomba1a1.png')
            elif self.frame is 1 and self.etype is 2:
                self.frame = 2
                self.pic = pygame.image.load('images/Goomba2a2.png')
            elif self.frame is 2 and self.etype is 2:
                self.frame = 1
                self.pic = pygame.image.load('images/Goomba2a1.png')
            self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def check_collisions(self, enemies, objects):
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

        # Collide with enemies as well
            for enemy in enemies:  # Only reposition to the sides
                if self.rect.colliderect(enemy) and self is not enemy:
                    if self.rect.right - enemy.rect.left < enemy.rect.right - self.rect.left:  # Reposition to the left
                        if self.x_direction is 1:  # When not moving left change direction to the left
                            self.x = enemy.rect.left - self.width
                            self.x_direction = -1
                    else:  # Reposition to the right
                        if self.x_direction is -1:  # When not moving right change direction to the right
                            self.x = enemy.rect.right
                            self.x_direction = 1
                    self.rect.x = self.x

    def take_damage(self):
        if not self.is_dead or not self.eliminated:
            self.ui.score += self.settings.goomba_points
        self.is_dead = True
        self.moment_of_death = self.timers.curtime
        pygame.mixer.Sound('sounds/stomp.ogg').play()
        if self.is_dead and self.etype is 1:
            self.pic = pygame.image.load('images/Goomba1d.png')
        elif self.is_dead and self.etype is 2:
            self.pic = pygame.image.load('images/Goomba2d.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def eliminate(self):
        if not self.is_dead or not self.eliminated:
            self.ui.score += self.settings.goomba_points
        self.is_dead = True
        self.eliminated = True
        pygame.mixer.Sound('sounds/kick.ogg').play()
        if self.etype is 1:
            self.pic = pygame.image.load('images/Goomba1d2.png')
            self.width = self.settings.goomba_width_death
            self.height = self.settings.goomba_height_death
        elif self.etype is 2:
            self.pic = pygame.image.load('images/Goomba2d2.png')
            self.width = self.settings.goomba_width_death
            self.height = self.settings.goomba_height_death
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
