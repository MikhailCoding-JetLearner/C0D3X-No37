import pygame
import os
import time
import random
pygame.init()
screen = pygame.display.set_mode((817, 435))
bg = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/fantasy night sky.png")
spaceship_player = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/spaceship player.png")
bullet = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/bullet_for_sci_fi_ship_player.png")
spaceship_enemy = pygame.image.load(r"/Users/Shiqin/Desktop/Folder of folders/Programmer's C0D3X containing PGZ3R0/images/spaceship enemy.png")
pygame.display.update()
enemyX = 100
enemyY = 100
playerx = 800
playery = 200
bulletx = 0
bullety = 0
additionals = 0
up = False
bullet_hit = pygame.Rect(bulletx, bullety, 20, 60)
spaceship_hit = pygame.Rect(enemyX, enemyY, 100, 100)
bulleter = []
def bulletes():
    global bulletx, bullety, up
    screen.blit(bullet, (bulletx, bullety))
    if up == True and bullety > 0:
        bullety -= 5
    else:
        up = False
def keys():
    global playerx, playery, bulletx, bullety, up
    everykeyz = pygame.key.get_pressed()
    if everykeyz[pygame.K_a]:
        playerx += -2
    if everykeyz[pygame.K_d]:
        playerx -= -2
    if everykeyz[pygame.K_w]:
        playery += -2
    if everykeyz[pygame.K_s]:
        playery -= -2
    if everykeyz[pygame.K_SPACE] and up == False:
        bulletx = playerx + 23
        bullety = playery
        up = True
def update():
    keys()
    bulletes()
while 1 == 1:
    print(up)
    screen.blit(bg, (0, 0))
    update()
    screen.blit(spaceship_player, (playerx, playery))

            
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
