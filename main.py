import pygame as pg
from settings import *
from sys import exit
from sprites import *

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH,HEIGHT))
        self.running = True
        self.playing = False
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.pipes = pg.sprite.Group()
        self.tick_count = 0


    def new(self):
        self.player = Player(50,400)
        self.all_sprites.add(self.player)
        self.playing = True
        self.run()

    def run(self):
        x = 0
        while self.playing:
            self.clock.tick(FPS)
            self.tick_count +=1
            self.events()
            self.scroll_background(x)
            self.update()
            x -=1
            if self.tick_count % 40 ==0:
                self.pipes.add(Pipe())
                    
    def scroll_background(self, x):
        rel_x = x % self.screen.get_rect().width
        self.screen.blit(pg.transform.scale(pg.image.load(BACKGROUND),(WIDTH,HEIGHT)),(rel_x - self.screen.get_rect().width,0))
        if rel_x < WIDTH:
            self.screen.blit(pg.transform.scale(pg.image.load(BACKGROUND),(WIDTH,HEIGHT)),(rel_x,0))      
                
           
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type ==pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def update(self):
        pg.display.update()
        self.all_sprites.draw(self.screen)
        self.pipes.draw(self.screen)
        self.pipes.update()
        self.player.update()
        pg.display.flip()

    def quit(self):
        if self.playing:
            self.playing = False
        self.running = False
        pg.quit()
        exit()
        
        


g = Game()
g.new()
while g.running:
    g.run()
g.quit()