import pygame as pg 
from settings import *
import random

class Player(pg.sprite.Sprite):
    def __init__(self, x, y):
       pg.sprite.Sprite.__init__(self)
       self.image = pg.image.load(BIRD)
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.velocity = 0
       self.gravity = .5


    def update(self):
        self.velocity -= self.gravity
        self.rect.y -= self.velocity
        
        if self.rect.y >= HEIGHT - 30:
            self.rect.y = HEIGHT -30
            self.velocity = 0

        if self.rect.y < 0:
            self.rect.y = 0
            self.velocity = 0

    def jump(self):
        self.velocity = self.gravity * 20

class Pipe(pg.sprite.Sprite):
    def __init__(self):
       pg.sprite.Sprite.__init__(self)
       self.image = pg.image.load(PIPE)
       self.rect = self.image.get_rect()
       self.rect.x = WIDTH - 100
       self.rect.y = random.choice([0,800- self.image.get_height()])
       self.speed = 5
    

    def update(self):
        self.rect.x -= self.speed

    