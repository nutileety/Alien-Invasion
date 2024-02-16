import pygame 
import sys
import random
import math
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800,600))
title = pygame.display.set_caption("Space Invaders")

# adding the background image
background = pygame.image.load('images/background.png')

#background music
mixer.music.load("audios/background.wav")
mixer.music.play(-1)

#setting the icon and image
icon = pygame.image.load('images/alien.png')
pygame.display.set_icon(icon)

#adding ship image 
playerImg = pygame.image.load('images/spaceship.png')
playerX =370
playerY = 480
playerX_change = 0  # variable for movement

# adding the i
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6
for i in range(no_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(1.5)
    enemyY_change.append(40)

# adding the bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
# bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

# displaying the score on the game window
score_value = 0
font = pygame.font.Font('freesansbold.ttf',25)
textX = 10
TextY = 10

# setting the game over text
over_font = pygame.font.Font('freesansbold.ttf',60)

# declaring all function below
def show_score(x,y):
    """setting font for the score"""
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def player(x,y):
    """ drawing the player to the screen """
    screen.blit(playerImg,(x,y))

def enemy(x,y,i):
    """ drawing the i to the screen """
    screen.blit(enemyImg[i],(x,y))

def fire_bullet(x,y):
    """function to draw a bullet and in 'fire' state"""
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y - 25))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    """calculating a shooting distance b/w i and th bullet collision"""
    distance = math.sqrt(((enemyX - bulletX)**2) + ((enemyY - bulletY) ** 2))
    if distance < 27:
        return True
    else:
        return False
    
def show_score(x,y):
    """function to show the score"""
    score = font.render("Score : "+str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER",True,(255,255,255))
    screen.blit(over_text,(200,250))

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
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3

            #shooting the bullet for space
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    shoot_sound = mixer.Sound("audios/shoot.wav")
                    shoot_sound.play()
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

    for i in range(no_of_enemies):
        # game over 
        if enemyY[i] > 450:
            for j in range(no_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break    
    
    # initialinzing the movement position of the ship
        enemyX[i] += enemyX_change[i]
        #setting boundary to the enemy
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 735:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]

         #calling the collision function and get to the initial state
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(score_value)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
            # adding blast sound
            blast_sound = mixer.Sound("audios/blast.wav")
            blast_sound.play()

        #calling the i function
        enemy(enemyX[i],enemyY[i],i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"    

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # calling the player functions 
    player(playerX,playerY)

    # calling the score function
    show_score(textX,TextY) 
    # display should be updated to save the change
    pygame.display.flip()