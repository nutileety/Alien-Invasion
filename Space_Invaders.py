import pygame 
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))
title = pygame.display.set_caption("Space Invaders")

#setting the icon and image
icon = pygame.image.load('images/alien.png')
pygame.display.set_icon(icon)

#adding ship image 
playerImg = pygame.image.load('images/spaceship.png')
playerX =370
playerY = 480
playerX_change = 0  # variable for movement

def player(x,y):
    """ drawing the player to the screen """
    screen.blit(playerImg,(x,y))

# the screen will not hold until it is not looped infinately.
while True:
     # adding color to the window
    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #condition to pressing a key indicates k_down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1

        #contion for releasing the key indicates k_up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
     
    # initialinzing the movement position
    playerX += playerX_change

    #setting boundary to the ship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # calling the player function 
    player(playerX,playerY)

    # display should be updated to save the change
    pygame.display.update()