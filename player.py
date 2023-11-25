import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('../graphics/player.png').convert_alpha()  #i need to create a folder called graphics containing a png for player
        self.rect = self.image.get_rect(midbottom=pos)