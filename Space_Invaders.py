import pygame 
import sys
import random

pygame.init()

screen = pygame.display.set_mode((800,600))
title = pygame.display.set_caption("Space Invaders")

# adding the background image
background = pygame.image.load('images/background.png')

#setting the icon and image
icon = pygame.image.load('images/alien.png')
pygame.display.set_icon(icon)

#adding ship image 
playerImg = pygame.image.load('images/spaceship.png')
playerX =370
playerY = 480
playerX_change = 0  # variable for movement

# adding the enemy
enemyImg = pygame.image.load('images/enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 1
enemyY_change = 40

# adding the bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"


def player(x,y):
    """ drawing the player to the screen """
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    """ drawing the enemy to the screen """
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y - 25))

# the screen will not hold until it is not looped infinately.
while True:
     # adding color and backgorund image to the window
    screen.fill((0,0,0))
    screen.blit(background,(0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        #condition to pressing a key indicates k_down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2

            #shooting the bullet for space
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                # bulletX is assigned by the position is x-coordinate of the player 
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)

        #contion for releasing the key indicates k_up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
     
    # initialinzing the movement position of the ship
    playerX += playerX_change

    #setting boundary to the ship
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # initialinzing the movement position of the ship
    enemyX += enemyX_change

    #setting boundary to the enemy
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"    

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # calling the functions 
    player(playerX,playerY)
    enemy(enemyX,enemyY)


    # display should be updated to save the change
    pygame.display.flip()