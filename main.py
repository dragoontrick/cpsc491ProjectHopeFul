import pygame, sys
from player import Player
#from player.py import Player class ^


#renamed clearcode example to main.py to better align with the example
class Game:
    def __init__(self): 
        player_sprite = Player((screen_width/2,screen_height),screen_width,5) #player at bottom middle screen, boundaryWidth, playerspeed
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def run(self):
        self.player.update()
        self.player.draw(screen)
        #update all sprite groups
        #draw all sprite groups

if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width,screen_height))
    clock = pygame.time.Clock()
    game = Game()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30,30,30))
    game.run() #this allos us to write the logic in the game class
    pygame.display.flip()
    clock.tick(60)