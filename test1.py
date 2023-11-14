#I will begin working on the project
import sys, pygame    #import libraries
pygame.init()           #initialize the library

size = width, height = 320, 240    #define the game window size
speed = [2, 2]                      #define The speed of how fast the ball will bounce
black = 0, 0, 0                     #define the color of the screen background

screen = pygame.display.set_mode(size)  #setup a screen

ball = pygame.image.load("intro_ball.gif")      #create a ball object
ballrect = ball.get_rect()                      #create a rectangle for hitbox detection for the ball.and apply to the ball object

while True:                                     #game loop
    for event in pygame.event.get():            #Waiting for an event like input
        if event.type == pygame.QUIT: sys.exit()        #if the event we receive is quit then exit the game.

    ballrect = ballrect.move(speed)             #The rectangle of the ball moves at the given speed.
    if ballrect.left < 0 or ballrect.right > width:     #if cant go further left then travel right and vice versa
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:       #if cant go further down, then travel up and vice versa.
        speed[1] = -speed[1]

    screen.fill(black)                          #background screen color
    screen.blit(ball, ballrect)                 #idk what blit means
    pygame.display.flip()                       #idk what flip means