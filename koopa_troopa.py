import pygame
from enemy import Enemy


class KoopaTroopa(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(KoopaTroopa, self).__init__(settings, screen, x, y, etype)

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

    def update_pos(self):
        self.x += self.settings.koopa_speed * self.x_direction
        self.y_velocity += self.settings.fall_acceleration
        self.y += self.y_velocity
        self.rect.x = self.x
        self.rect.y = self.y

    def update_image(self):
        # Alternate normal alive animation
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
                elif self.etype is 4:
                    self.pic = pygame.image.load('images/Koopa_Troopa4a2r.png')
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
                elif self.etype is 4:
                    self.pic = pygame.image.load('images/Koopa_Troopa4a1r.png')
                elif self.etype is 5:
                    self.pic = pygame.image.load('images/Koopa_Troopa5a1r.png')
                self.frame = 1
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
