import pygame
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
injY = 450
injX_change = 0

#virus

virusImg = pygame.image.load('virus.png')
virusX = random.randint(0, 360)
virusY = random.randint(40, 140)
virusX_change = 0.3
virusY_change = 40

#bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def inj(X,Y):
    screen.blit(injImg,(X,Y))

def virus(X,Y):
    screen.blit(virusImg,(X,Y))

def fire_bullet(X,Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(X+16 , Y+10))

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
                injX_change = -0.3
            if event.key == pygame.K_RIGHT:
                injX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
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
    virusX += virusX_change
    if virusX <= 0:
        virusX_change = 0.3
        virusY += virusY_change
    elif virusX >= 270:
        virusX_change = -0.3
        virusY += virusY_change
#bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    inj(injX,injY)
    virus(virusX, virusY)

    pygame.display.update()

