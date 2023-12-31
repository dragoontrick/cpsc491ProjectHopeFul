import pygame
from laser import Laser


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, constraint, yconstraint, speed):
        super().__init__()
        self.image = pygame.image.load("./graphics/player.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.speed = speed
        self.max_x_constraint = constraint
        self.ready = True
        self.laser_time = 0
        self.laser_cooldown = 600

        self.lasers = pygame.sprite.Group()

        self.laser_sound = pygame.mixer.Sound("./audio/laser.wav")
        self.laser_sound.set_volume(0.3)

        self.max_y_constraint = yconstraint

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += (
                self.speed
            )  # notice the .x for horizontal movement  .y should be verticle
        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        elif keys[pygame.K_UP]: #his tutorial doesnt have this but i need it later also need to add constraints for y axis
            self.rect.y -= self.speed

        elif keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready = False
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()
        if keys[pygame.K_LSHIFT]:
            pass
            #create a different attack which has pierce. we can make it have a cost in the main.py file. removing score value


    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_cooldown:
                self.ready = True

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x_constraint:
            self.rect.right = self.max_x_constraint

       # if self.rect.top >= 0: #constraint o this keeps my character locked to top of screen not what I want to happen
          #  self.rect.top = 0

    def shoot_laser(self):
        self.lasers.add(Laser(self.rect.center, -8, self.max_y_constraint))

    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()
        self.lasers.update()
