import pygame
from pygame.locals import *

class Player():
    def __init__(self, img, scale_fact, screen):
        self.img = pygame.image.load(img).convert_alpha()
        self.scale_factor = scale_fact
        self.img = pygame.transform.scale(self.img, scale_fact)
        self.screen = screen

        self.x = 600
        self.y = 450

        self.pos = self.y
        self.vel = 0

        self.acc = 9.81
        self.time_acc = 0
        self.acc_ongoing = False

    def velocity(self, delta_t):
        if (self.acc_ongoing == True):
            time_pass = pygame.time.get_ticks() - self.time_acc

            if (time_pass >= 1000):
                self.acc = 9.81
        self.vel = self.vel + self.acc * delta_t

        if (self.vel >= 40):
            self.vel = 40
        if (self.vel < -40):
            self.vel = -40

    def position(self, delta_t):
        self.pos = self.pos + self.vel * delta_t

        if (self.pos <= 0):
            self.pos = 0
        if ((self.pos + self.scale_factor[1]) >= self.screen.get_size()[1]):
            self.pos = self.screen.get_size()[1] - self.scale_factor[1]
        self.y = self.pos



    def jump(self):
        self.time_acc = pygame.time.get_ticks()
        self.acc = -10
        self.acc_ongoing = True


    def fall(self):
        if ((self.y + self.scale_factor[1]) <= screen.get_size()[1]):
            self.y = self.y + 5

    def print(self):
        self.screen.blit(self.img, (self.x, self.y))

