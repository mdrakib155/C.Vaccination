import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((360,640))

#Background image

background = pygame.image.load('background.png')

#title and logo

pygame.display.set_caption("C.Vacc")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

#Weapon

injImg = pygame.image.load('inj.png')
injX = 140
injY = 500
injX_change = 0

#virus

virusImg = []
virusX = []
virusY = []
virusX_change = []
virusY_change = []
num_of_viruses = 7

for i in range (num_of_viruses):
    virusImg.append (pygame.image.load('virus.png'))
    virusX.append( random.randint(0, 270))
    virusY.append( random.randint(40, 140))
    virusX_change.append (0.5)
    virusY_change.append (40)

#bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 420
bulletX_change = 0
bulletY_change = 1
bullet_state = "ready"

score = 0

def inj(X,Y):
    screen.blit(injImg,(X,Y))

def virus(X,Y,i):
    screen.blit(virusImg[i],(X,Y))

def fire_bullet(X,Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(X+33 , Y+2))

def isCollision(virusX, virusY, bulletX, bulletY):
    distance = math.sqrt(math.pow(virusX - bulletX, 2) + (math.pow(virusY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

#Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                injX_change = -1
            if event.key == pygame.K_RIGHT:
                injX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = injX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                injX_change = 0


    screen.blit(background, (0, 0))

    injX += injX_change
#Border
    if injX <= 0:
        injX = 0
    elif injX >= 270:
        injX = 270
#Movement of virus
    for i in range(num_of_viruses):
        virusX[i] += virusX_change[i]
        if virusX[i] <= 0:
            virusX_change[i] = 0.5
            virusY[i] += virusY_change[i]
        elif virusX[i] >= 270:
            virusX_change[i] = -0.5
            virusY[i] += virusY_change[i]

        collision = isCollision(virusX[i], virusY[i], bulletX, bulletY)
        if collision:
            bulletY = 420
            bullet_state = "ready"
            score += 1
            print(score)
            virusX[i] = random.randint(0, 270)
            virusY[i] = random.randint(40, 140)

        virus(virusX[i], virusY[i], i)

#bullet movement
    if bulletY <= 0:
        bulletY = 420
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    inj(injX,injY)
    pygame.display.update()

