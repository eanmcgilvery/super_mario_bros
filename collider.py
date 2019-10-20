import pygame

class Collider(pygame.sprite.Sprite):
    """Sprites placed overtop backgroud with objects that can be collided with such as pipe, or steps"""
    def __init__(self, x, y, width, height, name='collider'):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None