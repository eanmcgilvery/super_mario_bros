import pygame
from enemy import Enemy


class KoopaTroopa(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(KoopaTroopa, self).__init__(settings, screen, x, y, etype)

        """etype 1 is green koopa troopa, 2 is blue, 3 is red, 4 is flying red, 5 is jumping green"""
        # Rect, image, and initial position set up
        self.rect = pygame.Rect(x, y, settings.koopa_width, settings.koopa_height)
        if etype is 1:
            self.pic = pygame.image.load('images/Koopa1a1l.png')
        elif etype is 2:
            self.pic = pygame.image.load('images/Koopa2a1l.png')
        elif etype is 3:
            self.pic = pygame.image.load('images/Koopa3a1l.png')
        elif etype is 4:
            self.pic = pygame.image.load('images/Koopa4a1l.png')
        elif etype is 5:
            self.pic = pygame.image.load('images/Koopa5a1l.png')
        self.image = pygame.transform.scale(self.pic, (settings.koopa_width, settings.koopa_height))

    def update_pos(self):
        self.x += self.settings.koopa_speed * self.x_direction
        self.rect.x = self.x

    def update_image(self):
        # Alternate normal alive animation
        if self.x_direction is -1:
            if self.frame is 1:
                if self.etype is 1:
                    self.pic = pygame.image.load('images/Koopa1a2l.png')
                elif self.etype is 2:
                    self.pic = pygame.image.load('images/Koopa2a2l.png')
                elif self.etype is 3:
                    self.pic = pygame.image.load('images/Koopa3a2l.png')
                elif self.etype is 4:
                    self.pic = pygame.image.load('images/Koopa4a2l.png')
                elif self.etype is 5:
                    self.pic = pygame.image.load('images/Koopa5a2l.png')
                self.frame = 2
            elif self.frame is 2:
                if self.etype is 1:
                    self.pic = pygame.image.load('images/Koopa1a1l.png')
                elif self.etype is 2:
                    self.pic = pygame.image.load('images/Koopa2a1l.png')
                elif self.etype is 3:
                    self.pic = pygame.image.load('images/Koopa3a1l.png')
                elif self.etype is 4:
                    self.pic = pygame.image.load('images/Koopa4a1l.png')
                elif self.etype is 5:
                    self.pic = pygame.image.load('images/Koopa5a1l.png')
                self.frame = 1
        elif self.x_direction is 1:
            if self.frame is 1:
                if self.etype is 1:
                    self.pic = pygame.image.load('images/Koopa1a2r.png')
                elif self.etype is 2:
                    self.pic = pygame.image.load('images/Koopa2a2r.png')
                elif self.etype is 3:
                    self.pic = pygame.image.load('images/Koopa3a2r.png')
                elif self.etype is 4:
                    self.pic = pygame.image.load('images/Koopa4a2r.png')
                elif self.etype is 5:
                    self.pic = pygame.image.load('images/Koopa5a2r.png')
                self.frame = 2
            elif self.frame is 2:
                if self.etype is 1:
                    self.pic = pygame.image.load('images/Koopa1a1r.png')
                elif self.etype is 2:
                    self.pic = pygame.image.load('images/Koopa2a1r.png')
                elif self.etype is 3:
                    self.pic = pygame.image.load('images/Koopa3a1r.png')
                elif self.etype is 4:
                    self.pic = pygame.image.load('images/Koopa4a1r.png')
                elif self.etype is 5:
                    self.pic = pygame.image.load('images/Koopa5a1r.png')
                self.frame = 1
        self.image = pygame.transform.scale(self.pic, (self.settings.koopa_width, self.settings.koopa_height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
