import pygame
import math
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((360, 640))

# Background image

background = pygame.image.load('background.png')

mixer.music.load('background.wav')
mixer.music.play(-1)

# title and logo

pygame.display.set_caption("C.Vacc")
icon = pygame.image.load('logo.png')
pygame.display.set_icon(icon)

# Weapon

injImg = pygame.image.load('inj.png')
injX = 140
injY = 500
injX_change = 0

# virus

virusImg = []
virusX = []
virusY = []
virusX_change = []
virusY_change = []
num_of_viruses = 7

for i in range(num_of_viruses):
    virusImg.append(pygame.image.load('virus.png'))
    virusX.append(random.randint(0, 270))
    virusY.append(random.randint(40, 140))
    virusX_change.append(0.5)
    virusY_change.append(40)

# bullet

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 450
bulletX_change = 0
bulletY_change = 1.5
bullet_state = "ready"

# score

score_value = 0
font = pygame.font.Font('Alien-Encounters-Solid-Bold.ttf', 30)
textX = 8
textY = 8

over_font = pygame.font.Font('Alien-Encounters-Solid-Bold.ttf', 45)


def show_score(X, Y):
    score = font.render("score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (X, Y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (50, 280))


def inj(X, Y):
    screen.blit(injImg, (X, Y))


def virus(X, Y, i):
    screen.blit(virusImg[i], (X, Y))


def fire_bullet(X, Y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (X + 33, Y + 2))


def isCollision(virusX, virusY, bulletX, bulletY):
    distance = math.sqrt(math.pow(virusX - bulletX, 2) + (math.pow(virusY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # button
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                injX_change = -1
            if event.key == pygame.K_RIGHT:
                injX_change = 1
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('gun.mp3')
                    bullet_sound.play()
                    bulletX = injX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                injX_change = 0

    screen.blit(background, (0, 0))

    injX += injX_change
    # Border
    if injX <= 0:
        injX = 0
    elif injX >= 270:
        injX = 270
    # Movement of virus
    for i in range(num_of_viruses):

        if virusY[i] > 400:
            for j in range(num_of_viruses):
                virusY[j] = 2000
            game_over_text()
            break

        virusX[i] += virusX_change[i]
        if virusX[i] <= 0:
            virusX_change[i] = 0.5
            virusY[i] += virusY_change[i]
        elif virusX[i] >= 270:
            virusX_change[i] = -0.5
            virusY[i] += virusY_change[i]

        collision = isCollision(virusX[i], virusY[i], bulletX, bulletY)
        if collision:
            hurt_sound = mixer.Sound('hurt.mp3')
            hurt_sound.play()
            bulletY = 420
            bullet_state = "ready"
            score_value += 1
            virusX[i] = random.randint(0, 270)
            virusY[i] = random.randint(40, 140)

        virus(virusX[i], virusY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 420
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    inj(injX, injY)
    show_score(textX, textY)
    pygame.display.update()
