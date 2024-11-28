import pygame
from pygame.locals import *
import pygame.locals

class Obstacle:
    def __init__(self, img, coord, scale_factor, screen):
        self.coord = coord
        self.x = coord[0]
        self.y = coord[1]

        self.scale_factor = scale_factor
        self.screen = screen

        self.img = pygame.image.load(img).convert_alpha()
        self.img = pygame.transform.scale(self.img, scale_factor)

    def move(self):
        self.x = self.x - 2
        kill = False

        if ((self.x - self.scale_factor[0]) <= 0):
            kill = True
        
        return kill

    def print(self):
        self.screen.blit(self.img, (self.x, self.y))

