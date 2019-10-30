import pygame as pg


# Class that holds all of the attributes of our hero, Mario
class Mario(pg.sprite.Sprite):
    def __init__(self, settings, screen, ui, timers):
        pg.sprite.Sprite.__init__(self)

        self.jump_monitor = 0
        self.idle = True
        self.is_dead = False
        self.jump_ = False
        self.move_right = False
        self.move_left = False
        self.crouch = False
        self.run = False
        self.max_x_vel = 100
        self.curtime = pg.time.get_ticks()  # This should not be used
        self.timers = timers
        self.ui = ui

        self.allow_jump = True
        self.screen = screen
        self.settings = settings

        # Setup containers to hold the differing animations

        self.right_frames = [pg.image.load('images/mario_images/small_right/1.png'),
                             pg.image.load('images/mario_images/small_right/2.png'),
                             pg.image.load('images/mario_images/small_right/3.png')]

        # If small mario is standing still
        self.small_right_idle = pg.image.load('images/mario_images/small_right/0.png')
        self.small_left_idle = pg.transform.flip(self.small_right_idle, True, False)

        self.left_frames = []
        for frame in self.right_frames:
            image = pg.transform.flip(frame, True, False)
            self.left_frames.append(image)

        self.right_big_normal_frames = [pg.image.load('images/mario_images/big_right/0.png'),
                                        pg.image.load('images/mario_images/big_right/1.png'),
                                        pg.image.load('images/mario_images/big_right/2.png'),
                                        pg.image.load('images/mario_images/big_right/3.png')]

        self.left_big_normal_frames = []
        for frame in self.right_big_normal_frames:
            image = pg.transform.flip(frame, True, False)
            self.left_frames.append(image)

        self.right_fire_frames = [pg.image.load('images/mario_images/small_fire_right/0.png'),
                                  pg.image.load('images/mario_images/small_fire_right/1.png'),
                                  pg.image.load('images/mario_images/small_fire_right/2.png'),
                                  pg.image.load('images/mario_images/small_fire_right/3.png')]

        self.left_fire_frames = []
        for frame in self.right_fire_frames:
            image = pg.transform.flip(frame, True, False)
            self.left_fire_frames.append(image)

        # Variables that will update mario's speed

        self.y_velocity = 0
        self.x_velocity = 0

        # Size of Mario
        self.width = settings.mario_small_width
        self.height = settings.mario_small_height

        # Image list we will index through for animation
        self.index = 0
        self.image = pg.transform.scale(self.right_frames[self.index], (self.width, self.height))
        self.rect = pg.Rect(100, 500, self.width, self.height)

        # Start Mario on the Ground
        self.x = self.rect.x = 100
        self.y = self.rect.y = self.settings.ground_level - self.height

        self.center = float(self.rect.centerx)

        # Jumping attributes
        self.isJump = False
        self.jumpCount = 10

        self.facing_right = True
        self.crouching = False
        self.fire = False
        self.invincible = False
        self.super_size = False
        self.jump_denied = False
        self.death = False

    def animation(self, index_):
        """Return the correct images of Mario to animate through"""
        # Right facing images
        if self.facing_right and not self.idle:
            # Small mario facing right
            if not self.super_size:
                # Small regular mario
                self.image = pg.transform.scale(self.right_frames[index_], (self.width, self.height))
            # Big Mario facing right
            else:
                # Fire Mario
                if self.fire and not self.invincible:
                    self.image = pg.transform.scale(self.right_fire_frames[index_], (self.width, self.height))
                # Normal Super Mario
                elif not self.invincible and not self.fire:
                    self.image = pg.transform.scale(self.right_big_normal_frames[index_], (self.width, self.height))

        # Left facing images
        elif not self.facing_right and not self.idle:
            # Small mario facing right
            if not self.super_size:
                # Small regular mario
                self.image = pg.transform.scale(self.left_frames[index_], (self.width, self.height))
            # Big Mario facing right
            else:
                # Fire Mario
                if self.fire and not self.invincible:
                    self.image = pg.transform.scale(self.left_fire_frames[index_], (self.width, self.height))
                # Normal Super Mario
                elif not self.invincible and not self.fire:
                    self.image = pg.transform.scale(self.left_big_normal_frames[index_], (self.width, self.height))

        # Standing still right
        elif self.facing_right and self.idle:
            if not self.super_size:
                self.image = pg.transform.scale(self.small_right_idle, (self.width, self.height))
        # Standing still left
        else:
            if not self.super_size:
                self.image = pg.transform.scale(self.small_left_idle, (self.width, self.height))

    def check_collisions(self, enemies, objects, ui):
        if not self.death:
            for object_ in objects:
                if self.rect.colliderect(object_):
                    '''if object_.name == 'mushroom':
                        self.super_size = True
                    if object_.name == 'coin':
                        ui.score += 10'''
                    # Reposition Mario to the top of the object
                    if self.rect.bottom > object_.rect.top and self.y_velocity >= self.rect.bottom - object_.rect.top:
                        self.y = object_.rect.top - self.height
                        self.y_velocity = 0
                        self.allow_jump = True
                        # Reposition to the bottom
                    elif object_.rect.bottom > self.rect.top and self.y_velocity * -1 >= object_.rect.bottom - \
                            self.rect.top:
                        self.y = object_.rect.bottom
                        self.y_velocity = 0
                        if self.super_size:
                            self.break_bricks()
                    elif self.rect.right - object_.rect.left < object_.rect.right - self.rect.left:  # Reposition to
                        # the left
                        self.x = object_.rect.left - self.width
                        self.move_right = False
                    else:  # Reposition to the right
                        self.x = object_.rect.right
                        self.move_left = False
                    self.rect.x = self.x
                    self.rect.y = self.y

            # Mario collision with enemy behaviors
            for enemy in enemies:
                if self.rect.colliderect(enemy):
                    if not enemy.eliminated:
                        if enemy.ename is "koopa_troopa" and enemy.is_dead and not enemy.moving:
                            if self.rect.centerx < enemy.rect.centerx:
                                enemy.x_direction = 1
                            else:
                                enemy.x_direction = -1
                            self.ui.score += self.settings.shell_kick_points
                            enemy.moving = True
                            self.timers.last_shell_kick = self.timers.curtime
                            pg.mixer.Sound('sounds/kick.ogg').play()
                        elif self.rect.bottom > enemy.rect.top and self.y_velocity >= self.rect.bottom - enemy.rect.top:
                            # Bounce off the top (in most cases)
                            if enemy.ename is "goomba" and not enemy.is_dead or enemy.ename is "koopa_troopa" and not \
                                    enemy.is_dead:
                                self.y = enemy.rect.top - self.height
                                self.y_velocity = self.settings.enemy_jump_speed / 2
                                enemy.take_damage()
                            elif enemy.ename is "koopa_troopa" and enemy.is_dead and enemy.moving:
                                self.y = enemy.rect.top - self.height
                                self.y_velocity = self.settings.enemy_jump_speed / 2
                                enemy.moving = False
                                enemy.take_damage()
                        else:  # Touching sides or bottom of enemies
                            if enemy.ename is "koopa_troopa" or enemy.ename is "goomba":
                                # Mario takes damage
                                if not self.super_size and not self.invincible:
                                    if enemy.ename is "goomba" and enemy.is_dead:
                                        pass
                                    elif not (enemy.ename is "koopa_troopa" and enemy.moving and (self.timers.curtime - self.timers.last_shell_kick > self.timers.shell_kick_wait)):
                                        pass
                                    else:
                                        self.is_dead = True
                                        self.fire = False
                                        self.death_sequence()
                                elif self.invincible:
                                    pass
                                else:
                                    self.super_size = False
                                    self.fire = False

                            elif enemy.is_dead:
                                # Do nothing
                                pass
                            else:
                                # Mario takes damage
                                pass

    def death_sequence(self):
        if self.is_dead:
            self.ui.lives -= 1
            pg.mixer.Sound('sounds/death.wav').play()
            self.image = pg.image.load('images/mario_images/mario_death.png')
            self.image = pg.transform.scale(self.image, (self.width, self.height))

            # Mario slightly hops up
            self.y -= 15

            # Mario falls through the floor
            while self.y < self.settings.screen_height:
                self.y += self.settings.fall_acceleration - .8

    def animation_speed(self):
        """Used to make walking animation speed be in relation to
        Mario's x-vel"""
        if self.x_velocity == 0:
            animation_speed = 130
        elif self.x_velocity > 0:
            animation_speed = 130 - (self.x_velocity * 13)
        else:
            animation_speed = 130 - (self.x_velocity * 13 * -1)
        return animation_speed

    def movement(self, settings):
        # Move right or left
        if self.move_right:
            if self.run:
                self.x += settings.RUN_SPEED
            else:
                self.x += settings.WALK_SPEED
        elif self.move_left and self.rect.left > 0:
            if self.run:
                self.x -= settings.RUN_SPEED
            else:
                self.x -= settings.WALK_SPEED

    def update_pos(self, enemies, objects, settings, ui):
        if not self.death:
            # Constantly add a downward gravity force
            self.y_velocity += self.settings.fall_acceleration
            if not self.jump_:
                self.y += self.y_velocity
                self.jumpCount = 12

            self.rect.x = self.x
            self.rect.y = self.y

            # Check movement
            self.movement(settings)

            # Jump with spacebar
            if self.jump_ and self.jump_monitor == 0:
                if not self.super_size:
                    self.image = pg.image.load("images/mario_images/mario_small_jump.png")
                    self.image = pg.transform.scale(self.image, (self.width, self.height))
                    if not self.facing_right:
                        self.image = pg.transform.flip(self.image, True, False)
                else:
                    self.image = pg.image.load("images/mario_images/mario_big_jump.png")
                    self.image = pg.transform.scale(self.image, (self.width, self.height))
                # Force added to jump
                if self.jumpCount > -1:
                    self.y -= (self.jumpCount * abs(self.jumpCount)) * 0.5
                    self.jumpCount -= 2

                # self.allow_jump = False
            self.check_collisions(enemies, objects, ui)
            self.rect.x = self.x
            self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move_with_screen(self, screen_x_move):
        self.x -= screen_x_move
        self.rect.x = self.x

    def break_bricks(self):
        pass
