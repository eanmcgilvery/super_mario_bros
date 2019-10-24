import pygame
from object import Object

class Pipe(Object):
    def __init__(self, settings, screen, x, y, otype):
        super(Pipe, self).__init__(settings, screen, x, y, otype)

        # Rect, image, and initial position set up
        if self.otype is 1:
            self.pic = pygame.image.load('images/pipe1.png')
            self.rect = pygame.Rect(x, y, settings.small_pipe_width, settings.small_pipe_height)
            self.image = pygame.transform.scale(self.pic, (settings.small_pipe_width, settings.small_pipe_height))
        elif self.otype is 2:
            self.pic = pygame.image.load('images/pipe2.png')
            self.rect = pygame.Rect(x, y, settings.medium_pipe_width, settings.medium_pipe_height)
            self.image = pygame.transform.scale(self.pic, (settings.medium_pipe_width, settings.medium_pipe_height))
        elif self.otype is 3:
            self.pic = pygame.image.load('images/pipe3.png')
            self.rect = pygame.Rect(x, y, settings.large_pipe_width, settings.large_pipe_height)
            self.image = pygame.transform.scale(self.pic, (settings.large_pipe_width, settings.large_pipe_height))

    def update_image(self):
        self.image = self.image

    def blitme(self):
        self.screen.blit(self.image, self.rect)