import pygame as pg
from settings import *
from sys import exit
from sprites import *
import random
import time


class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        pg.font.init()
        self.mixer = pg.mixer.init()
        self.font = pg.font.Font(pg.font.get_default_font(), 40)
        self.running = True
        self.playing = False
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.Group()
        self.pipes = pg.sprite.Group()
        self.tick_count = 0
        self.score = 0

    def new(self):
        self.reset()
        self.player = Player(self, 50, 400)
        self.all_sprites.add(self.player)
        self.screen.blit(pg.transform.scale(
            BACKGROUND, (WIDTH, HEIGHT)), (0, 0))
        self.draw_base()

    def reset(self):
        self.all_sprites.empty()
        self.player = None
        self.score = 0
        self.pipes.empty()

    def run(self):
        x = 0
        while self.playing:
            self.clock.tick(FPS)
            self.tick_count += 1
            self.events()
            if self.tick_count % 50 == 0:
                difference = random.choice(range(0, BASE.get_height()))
                self.pipes.add(Pipe(self, 0 - difference))
                self.pipes.add(
                    Pipe(self, 800 - PIPE.get_height() - difference))
            self.scroll_background(x)
            self.draw_base()
            self.update()
            x -= 1

    def scroll_background(self, x):
        rel_x = x % self.screen.get_rect().width
        self.screen.blit(pg.transform.scale(
            BACKGROUND, (WIDTH, HEIGHT)), (rel_x - self.screen.get_rect().width, 0))

        if rel_x < WIDTH:
            self.screen.blit(pg.transform.scale(
                BACKGROUND, (WIDTH, HEIGHT)), (rel_x, 0))

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def start_screen(self):
        start_text = self.font.render("Start", True, (255, 255, 255))
        start_text_rect = start_text.get_rect()
        start_text_rect.center = (
            self.screen.get_width() // 2, self.screen.get_height() // 2)
        self.screen.blit(start_text, start_text_rect)
        while not self.playing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.playing = True
            pg.display.update()

    def dead_screen(self):
        texts = ["Restart", f"Score: {str(int(self.score / 2))}", "You Died"]
        for index, text in enumerate(texts):
            dead_text = self.font.render(text, True, (255, 255, 255))
            dead_text_rect = dead_text.get_rect()
            dead_text_rect.center = (
                self.screen.get_width() // 2, self.screen.get_height() // 2 - index * 50)
            self.screen.blit(dead_text, dead_text_rect)
        while not self.playing:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.quit()

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        self.playing = True
            pg.display.update()
        self.new()

    def score_count(self):
        score_text = self.font.render(
            f"Score: {str(int(self.score /2))}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (200 // 2, 60 // 2)
        self.screen.blit(score_text, score_text_rect)

    def draw_base(self):
        self.screen.blit(pg.transform.scale(
            BASE, (WIDTH, BASE.get_height())), (0, HEIGHT - BASE.get_height()))

    def update(self):
        self.all_sprites.draw(self.screen)
        self.pipes.draw(self.screen)
        self.draw_base()
        self.pipes.update()
        self.player.update()
        self.score_count()
        pg.display.update()

    def quit(self):
        if self.playing:
            self.playing = False
        self.running = False
        pg.quit()
        exit()


g = Game()
g.new()
g.start_screen()
while g.running:
    g.run()
g.quit()
