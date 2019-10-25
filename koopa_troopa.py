import pygame
from enemy import Enemy


class KoopaTroopa(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(KoopaTroopa, self).__init__(settings, screen, x, y, etype, ename="koopa_troopa")

        self.width = settings.koopa_width
        self.height = settings.koopa_height
        """etype 1 is green koopa troopa, 2 is blue, 3 is red, 4 is flying red, 5 is jumping green"""
        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, self.width, self.height)
        if etype is 1:
            self.pic = pygame.image.load('images/Koopa_Troopa1a1l.png')
        elif etype is 2:
            self.pic = pygame.image.load('images/Koopa_Troopa2a1l.png')
        elif etype is 3:
            self.pic = pygame.image.load('images/Koopa_Troopa3a1l.png')
        elif etype is 4:
            self.pic = pygame.image.load('images/Koopa_Troopa4a1l.png')
        elif etype is 5:
            self.pic = pygame.image.load('images/Koopa_Troopa5a1l.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def update_pos(self, objects):
        if not self.is_dead:
            self.x += self.settings.koopa_speed * self.x_direction
        self.y_velocity += self.settings.fall_acceleration
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y
        self.check_collisions(objects)

    def update_image(self, changeframe):
        if not self.is_dead:
            # Alternate normal alive animation
            if changeframe:
                pass
            else:  # Update the image but do not change its place in animation
                if self.frame is 1:
                    self.frame = 2
                else:
                    self.frame = 1
            if self.x_direction is -1:
                if self.frame is 1:
                    if self.etype is 1:
                        self.pic = pygame.image.load('images/Koopa_Troopa1a2l.png')
                    elif self.etype is 2:
                        self.pic = pygame.image.load('images/Koopa_Troopa2a2l.png')
                    elif self.etype is 3:
                        self.pic = pygame.image.load('images/Koopa_Troopa3a2l.png')
                    elif self.etype is 4:
                        self.pic = pygame.image.load('images/Koopa_Troopa4a2l.png')
                    elif self.etype is 5:
                        self.pic = pygame.image.load('images/Koopa_Troopa5a2l.png')
                    self.frame = 2
                elif self.frame is 2:
                    if self.etype is 1:
                        self.pic = pygame.image.load('images/Koopa_Troopa1a1l.png')
                    elif self.etype is 2:
                        self.pic = pygame.image.load('images/Koopa_Troopa2a1l.png')
                    elif self.etype is 3:
                        self.pic = pygame.image.load('images/Koopa_Troopa3a1l.png')
                    elif self.etype is 4:
                        self.pic = pygame.image.load('images/Koopa_Troopa4a1l.png')
                    elif self.etype is 5:
                        self.pic = pygame.image.load('images/Koopa_Troopa5a1l.png')
                    self.frame = 1
            elif self.x_direction is 1:
                if self.frame is 1:
                    if self.etype is 1:
                        self.pic = pygame.image.load('images/Koopa_Troopa1a2r.png')
                    elif self.etype is 2:
                        self.pic = pygame.image.load('images/Koopa_Troopa2a2r.png')
                    elif self.etype is 3:
                        self.pic = pygame.image.load('images/Koopa_Troopa3a2r.png')
                    elif self.etype is 5:
                        self.pic = pygame.image.load('images/Koopa_Troopa5a2r.png')
                    self.frame = 2
                elif self.frame is 2:
                    if self.etype is 1:
                        self.pic = pygame.image.load('images/Koopa_Troopa1a1r.png')
                    elif self.etype is 2:
                        self.pic = pygame.image.load('images/Koopa_Troopa2a1r.png')
                    elif self.etype is 3:
                        self.pic = pygame.image.load('images/Koopa_Troopa3a1r.png')
                    elif self.etype is 5:
                        self.pic = pygame.image.load('images/Koopa_Troopa5a1r.png')
                    self.frame = 1
            self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def check_collisions(self, objects):
        changeframe = False
        for object in objects:
            if self.rect.colliderect(object):
                if self.rect.bottom > object.rect.top and self.y_velocity >= self.rect.bottom - object.rect.top:  # Reposition koopa troopa to the top of the object
                    self.y = object.rect.top - self.height
                    self.y_velocity = 0
                    if self.etype is 5:
                        self.y_velocity = self.settings.enemy_jump_speed
                elif object.rect.bottom > self.rect.top and self.y_velocity * -1 >= object.rect.bottom - self.rect.top:  # Reposition to the bottom
                    self.y = object.rect.bottom
                    self.y_velocity = 0
                elif self.rect.right - object.rect.left < object.rect.right - self.rect.left:  # Reposition to the left
                    if self.x_direction is 1:  # When not moving left change direction to the left
                        self.x = object.rect.left - self.width
                        self.x_direction = -1
                        self.update_image(changeframe)
                else:  # Reposition to the right
                    if self.x_direction is -1:  # When not moving right change direction to the right
                        self.x = object.rect.right
                        self.x_direction = 1
                        self.update_image(changeframe)
                self.rect.x = self.x
                self.rect.y = self.y

    def take_damage(self):
        if self.etype is 1 or self.etype is 2 or self.etype is 3:
            self.is_dead = True
            if self.etype is 1:
                self.pic = pygame.image.load('images/Koopa_Troopa1d1.png')
            elif self.etype is 2:
                self.pic = pygame.image.load('images/Koopa_Troopa2d1.png')
            elif self.etype is 3:
                self.pic = pygame.image.load('images/Koopa_Troopa3d1.png')
            self.width = self.settings.dead_koopa_width
            self.height = self.settings.dead_koopa_height
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        elif self.x_direction is -1:
            if self.etype is 4:
                self.etype = 3
                if self.frame is 1:
                    self.frame = 2
                    self.pic = pygame.image.load('images/Koopa_Troopa3a1l.png')
                elif self.frame is 2:
                    self.frame = 1
                    self.pic = pygame.image.load('images/Koopa_Troopa3a2l.png')
            elif self.etype is 5:
                self.etype = 1
                if self.frame is 1:
                    self.frame = 2
                    self.pic = pygame.image.load('images/Koopa_Troopa1a1l.png')
                elif self.frame is 2:
                    self.frame = 1
                    self.pic = pygame.image.load('images/Koopa_Troopa1a2l.png')
            if self.y_velocity < 0:
                self.y_velocity = 0
        elif self.x_direction is 1:
            if self.etype is 4:
                self.etype = 3
                if self.frame is 1:
                    self.frame = 2
                    self.pic = pygame.image.load('images/Koopa_Troopa3a1r.png')
                elif self.frame is 2:
                    self.frame = 1
                    self.pic = pygame.image.load('images/Koopa_Troopa3a2r.png')
            elif self.etype is 5:
                self.etype = 1
                if self.frame is 1:
                    self.frame = 2
                    self.pic = pygame.image.load('images/Koopa_Troopa1a1r.png')
                elif self.frame is 2:
                    self.frame = 1
                    self.pic = pygame.image.load('images/Koopa_Troopa1a2r.png')
            if self.y_velocity < 0:
                self.y_velocity = 0
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
