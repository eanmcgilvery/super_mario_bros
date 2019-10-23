import pygame
from enemy import Enemy


class FakeBowser(Enemy):
    def __init__(self, settings, screen, x, y, etype):
        super(FakeBowser, self).__init__(settings, screen, x, y, etype)

        # Rect, image, and initial position set up
        self.width = settings.fake_bowser_width
        self.height = settings.fake_bowser_height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.pic = pygame.image.load('images/Fake_Bowsera1l.png')
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

        # Always faces mario regardless of which direction he moves
        self.facing_left = True

    def update_pos(self):
        self.x += self.settings.fake_bowser_speed * self.x_direction
        self.rect.x = self.x

    def update_image(self):
        # Alternate normal alive animation
        if self.facing_left:
            if self.frame is 1:
                self.pic = pygame.image.load('images/Fake_Bowsera2l.png')
                self.frame = 2
            elif self.frame is 2:
                self.pic = pygame.image.load('images/Fake_Bowsera1l.png')
                self.frame = 1
        elif not self.facing_left:
            if self.frame is 1:
                self.pic = pygame.image.load('images/Fake_Bowsera2r.png')
                self.frame = 2
            elif self.frame is 2:
                self.pic = pygame.image.load('images/Fake_Bowsera1r.png')
                self.frame = 1
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
