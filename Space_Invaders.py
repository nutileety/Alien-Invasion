import pygame 
import sys

pygame.init()

screen = pygame.display.set_mode((1000,800))
title = pygame.display.set_caption("This is a window")

#setting the icon and image
icon = pygame.image.load("Alien_Invasion/images/ship2.png")
pygame.display.set_icon(icon)

#adding ship image 
playerImg = pygame.image.load('Alien_Invasion/images/spaceship.png')
playerX =500
playerY = 700

def player():
    """ drawing the player to the screen """
    screen.blit(playerImg,(playerX,playerY))

# the screen will not hold until it is not looped infinately.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
    # adding color to the window
    screen.fill((230,230,230))

    # calling the player function 
    player()

    # display should be updated to save the change
    pygame.display.flip()