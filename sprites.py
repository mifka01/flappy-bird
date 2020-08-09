import pygame as pg 
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
       pg.sprite.Sprite.__init__(self)
       self.game = game
       self.pipes = self.game.pipes
       self.images = [BIRD1, BIRD2, BIRD3]
       self. index = 0 
       self.image = self.images[self.index]
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y
       self.velocity = 0
       self.gravity = .5

    def update(self):
        self.animations()
        self.velocity -= self.gravity
        self.rect.y -= self.velocity
        self.colisions()

    def animations(self):
        self.index +=1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        
    def jump(self):
        self.velocity = self.gravity * 20
        
        JUMP_SOUND.play()
        
 
    def colisions(self):
        if self.rect.y >= HEIGHT - BASE.get_height() - BIRD1.get_height():
            self.rect.y = HEIGHT - BASE.get_height() - BIRD1.get_height()
            self.velocity = 0
            DIE_SOUND.play()
            self.game.playing = False
            self.game.dead_screen()

        if self.rect.y < 0:
            self.rect.y = 0
            self.velocity = 0
            DIE_SOUND.play() 
            self.game.playing = False
            self.game.dead_screen()

        if pg.sprite.spritecollideany(self, self.pipes):
            DIE_SOUND.play()
            self.game.playing = False
            self.game.dead_screen()


class Pipe(pg.sprite.Sprite):
    def __init__(self, game: object, y):
       pg.sprite.Sprite.__init__(self)
       self.game = game
       self.pipes = game.pipes
       self.image = PIPE
       self.rect = self.image.get_rect()
       self.rect.x = WIDTH - 100
       self.rect.y = y
       self.speed = 5
       self.flip_image()
    
    def update(self):
        self.rect.x -= self.speed
        if self.rect.x < 0:
            self.pipes.remove(self)
            self.game.score += 1
            POINT_SOUND.play()

    def flip_image(self):
        if self.rect.y <= 0:
            self.image = pg.transform.flip(self.image,False,True)

    