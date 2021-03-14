import pygame

pygame.init()

screen = pygame.display.set_mode((360,640))

#Background image

background = pygame.image.load('background.png')

#title and logo

pygame.display.set_caption("C.Vacc")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)


#Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill((255, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.update()

