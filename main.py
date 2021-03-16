import pygame

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
virusX = 140
virusY = 40
virusX_change = 0

def inj(X,Y):
    screen.blit(injImg,(X,Y))

def virus(X,Y):
    screen.blit(virusImg,(X,Y))

#Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                injX_change = -0.3
            if event.key == pygame.K_RIGHT:
                injX_change = 0.3
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

    inj(injX,injY)
    virus(virusX, virusY)
    pygame.display.update()

