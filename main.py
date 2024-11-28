import pygame
from pygame.locals import *

import player as Player
import obstacle as Obstacle

res_x = 1200
res_y = 900

pygame.init()

screen = pygame.display.set_mode((res_x, res_y))

bkgrd = pygame.image.load("./graphics/environment/background.png")
bkgrd = pygame.transform.scale(bkgrd, (res_x, res_y))

player = Player.Player("./graphics/plane/red0.png", (100,100), screen)

obstacle = Obstacle.Obstacle("./graphics/obstacles/0.png", (600,450), (150,200), screen)
start_time = pygame.time.get_ticks()

run = True
while run:

    finish_time = pygame.time.get_ticks()
    delta_t = finish_time - start_time
    player.velocity(delta_t/100)
    player.position(delta_t/100)    

    start_time = finish_time

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        player.jump()
    
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            run = False
        
        if ev.type == pygame.MOUSEBUTTONDOWN:
            player.jump()

    obstacle.move()

    screen.blit(bkgrd, (0, 0))
    obstacle.print()
    player.print()
    pygame.display.flip()

