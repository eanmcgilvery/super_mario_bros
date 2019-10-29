import pygame
from enemy import Enemy


class KoopaTroopa(Enemy):
    def __init__(self, settings, screen, ui, timers, x, y, etype):
        super(KoopaTroopa, self).__init__(settings, screen, ui, timers, x, y, etype, ename="koopa_troopa")

        self.width = settings.koopa_width
        self.height = settings.koopa_height
        self.moment_of_death = 0
        self.last_leg_kick = 0
        self.moving = False

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

    def update_pos(self, enemies, objects):
        if not self.eliminated:
            if not self.is_dead:
                self.x += self.settings.koopa_speed * self.x_direction
            elif self.is_dead and self.moving:
                self.x += self.settings.koopa_shell_speed * self.x_direction
            self.y_velocity += self.settings.fall_acceleration
            self.y += self.y_velocity
            self.rect.x = self.x
            self.rect.y = self.y
            self.check_collisions(enemies, objects)
        else:
            self.y_velocity += self.settings.fall_acceleration
            self.y += self.y_velocity
            self.rect.x = self.x
            self.rect.y = self.y

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

    def check_collisions(self, enemies, objects):
        if not self.eliminated:
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
                            if self.moving:
                                pygame.mixer.Sound('sounds/bump.ogg').play()
                    else:  # Reposition to the right
                        if self.x_direction is -1:  # When not moving right change direction to the right
                            self.x = object.rect.right
                            self.x_direction = 1
                            self.update_image(changeframe)
                            if self.moving:
                                pygame.mixer.Sound('sounds/bump.ogg').play()
                    self.rect.x = self.x
                    self.rect.y = self.y

        # Collide with enemies as well
            for enemy in enemies:  # Only reposition to the sides
                if self.rect.colliderect(enemy) and self is not enemy:
                    if enemy.eliminated:
                        pass
                    elif self.moving:
                        enemy.eliminate()
                    elif self.rect.right - enemy.rect.left < enemy.rect.right - self.rect.left:  # Reposition to the left
                        if self.x_direction is 1:  # When not moving left change direction to the left
                            self.x = enemy.rect.left - self.width
                            self.x_direction = -1
                            self.update_image(changeframe)
                    else:  # Reposition to the right
                        if self.x_direction is -1:  # When not moving right change direction to the right
                            self.x = enemy.rect.right
                            self.x_direction = 1
                            self.update_image(changeframe)
                    self.rect.x = self.x

    def take_damage(self):
        changeframe = False
        self.ui.score += self.settings.koopa_points
        pygame.mixer.Sound('sounds/stomp.ogg').play()
        if self.etype is 1 or self.etype is 2 or self.etype is 3:
            self.is_dead = True
            self.moment_of_death = self.timers.curtime
            self.frame = 2
            if self.etype is 1:
                self.pic = pygame.image.load('images/Koopa_Troopa1d1.png')
            elif self.etype is 2:
                self.pic = pygame.image.load('images/Koopa_Troopa2d1.png')
            elif self.etype is 3:
                self.pic = pygame.image.load('images/Koopa_Troopa3d1.png')
            self.width = self.settings.dead_koopa_width
            self.height = self.settings.dead_koopa_height
            self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
            self.image = pygame.transform.scale(self.pic, (self.width, self.height))
        elif self.etype is 4:
            self.etype = 3
            self.update_image(changeframe)
        elif self.etype is 5:
            self.etype = 1
            self.update_image(changeframe)
        if self.y_velocity < 0:
            self.y_velocity = 0

    def reanimate(self):
        if self.is_dead and not self.eliminated and not self.moving:
            if self.timers.curtime - self.moment_of_death > self.timers.koopa_reanimate_wait:
                if self.timers.curtime - self.moment_of_death > self.timers.koopa_come_back_wait:
                    changeframe = False
                    self.frame = 1
                    self.height = self.settings.koopa_height
                    self.y -= self.settings.koopa_height / 3
                    self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                    self.is_dead = False
                    self.update_image(changeframe)
                elif self.timers.curtime - self.last_leg_kick > self.timers.koopa_legs_wait:
                    self.last_leg_kick = self.timers.curtime
                    if self.frame is 1:
                        self.frame = 2
                        if self.etype is 1:
                            self.pic = pygame.image.load('images/Koopa_Troopa1d1.png')
                        elif self.etype is 2:
                            self.pic = pygame.image.load('images/Koopa_Troopa2d1.png')
                        elif self.etype is 3:
                            self.pic = pygame.image.load('images/Koopa_Troopa3d1.png')
                    elif self.frame is 2:
                        self.frame = 1
                        if self.etype is 1:
                            self.pic = pygame.image.load('images/Koopa_Troopa1d2.png')
                        elif self.etype is 2:
                            self.pic = pygame.image.load('images/Koopa_Troopa2d2.png')
                        elif self.etype is 3:
                            self.pic = pygame.image.load('images/Koopa_Troopa3d2.png')
                    self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def eliminate(self):
        if not self.eliminated:
            self.ui.score += self.settings.koopa_points
        self.is_dead = True
        self.eliminated = True
        if self.y_velocity < 0:
            self.y_velocity = 0
        if self.etype is 1 or self.etype is 5:
            self.pic = pygame.image.load('images/Koopa_Troopa1d3.png')
        elif self.etype is 2:
            self.pic = pygame.image.load('images/Koopa_Troopa2d3.png')
        elif self.etype is 3 or self.etype is 4:
            self.pic = pygame.image.load('images/Koopa_Troopa3d3.png')
        self.width = self.settings.dead_koopa_width
        self.height = self.settings.dead_koopa_height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.image = pygame.transform.scale(self.pic, (self.width, self.height))

    def blitme(self):
        self.screen.blit(self.image, self.rect)
