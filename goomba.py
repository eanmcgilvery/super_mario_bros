import pygame
from enemy import Enemy


class Goomba(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(Goomba, self).__init__(settings, screen, x, y, etype, ename="goomba")

        self.width = settings.goomba_width
        self.height = settings.goomba_height
        """etype 1 is brown goomba, 2 is blue goomba"""
        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, self.width, self.height)
        if etype is 1:
            self.pic = pygame.image.load('images/Goomba1a1.png')
        elif etype is 2:
            self.pic = pygame.image.load('images/Goomba2a1.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def update_pos(self, objects):
        if not self.is_dead:
            self.x += self.settings.goomba_speed * self.x_direction
        self.y_velocity += self.settings.fall_acceleration
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
        self.check_collisions(objects)

    def update_image(self):
        # Alternate normal alive animation
        if not self.is_dead:
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

    def check_collisions(self, objects):
        for object in objects:
            overlap = 9999
            repos = ""
            if self.rect.colliderect(object):
                if self.rect.bottom > object.rect.top:
                    if overlap > self.rect.bottom - object.rect.top:
                        overlap = self.rect.bottom - object.rect.top
                        repos = "top"
                if object.rect.bottom > self.rect.top:
                    if overlap > object.rect.bottom - self.rect.top:
                        overlap = object.rect.bottom - self.rect.top
                        repos = "bottom"
                if self.rect.right > object.rect.left:
                    if overlap > self.rect.right - object.rect.left:
                        overlap = self.rect.right - object.rect.left
                        repos = "left"
                if object.rect.right > self.rect.left:
                    if overlap > object.rect.right - self.rect.left:
                        overlap = object.rect.right - self.rect.left
                        repos = "right"
                if repos is "top":
                    self.rect.bottom -= overlap
                    self.y_velocity = 0
                elif repos is "bottom":
                    self.rect.top += overlap
                    self.y_velocity = 0
                elif repos is "left":
                    self.rect.right -= overlap
                    self.x_direction *= -1
                elif repos is "right":
                    self.rect.left += overlap
                    self.x_direction *= -1

    def take_damage(self):
        self.is_dead = True
        if self.is_dead and self.etype is 1:
            self.pic = pygame.image.load('images/Goomba1d.png')
        elif self.is_dead and self.etype is 2:
            self.pic = pygame.image.load('images/Goomba2d.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
