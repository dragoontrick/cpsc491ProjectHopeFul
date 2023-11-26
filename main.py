import pygame, sys
from player import Player
#from player.py import Player class ^
import obstacle

#renamed clearcode example to main.py to better align with the example
class Game:
    def __init__(self): 
        #playersetup
        player_sprite = Player((screen_width/2,screen_height),screen_width,screen_height, 5) #player at bottom middle screen, boundaryWidth, playerspeed
        self.player = pygame.sprite.GroupSingle(player_sprite)

        #obstacle setup
        self.shape = obstacle.shape
        self.block_size = 6
        self.blocks = pygame.sprite.Group()
        self.obstacle_amount = 4
        self.obstacle_x_positions = [num *(screen_width/self.obstacle_amount) for num in range(self.obstacle_amount)] #0,1,2,3 and gets a position 
        self.create_multiple_obstacles(*self.obstacle_x_positions,x_start= screen_width/15, y_start= 380)  #values 0,100,200 are all part of offset tuple *unpacks

    def create_obstacle(self, x_start, y_start, offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col =='x':
                    x = x_start + col_index * self.block_size + offset_x
                    y = y_start + row_index * self.block_size
                    block = obstacle.Block(self.block_size,(241,79,80),x,y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self,*offset, x_start,y_start):
        for offset_x in offset:
            self.create_obstacle(x_start,y_start,offset_x)

    def run(self):
        self.player.sprite.lasers.draw(screen)
        self.player.update()
        self.player.draw(screen)
    
        self.blocks.draw(screen)
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