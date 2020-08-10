import pygame as pg
from settings import *
from sys import exit
from sprites import *
import random
import time


class Game:
    """Application instance.
    Attributes:
    ----------
    screen: pygame display object (surface) \n
    mixer: pygame audio object (mixer) \n
    font: pygame font object (font) \n
    running: boolean \n
    playing: boolean \n
    clock: pygame clock object (Clock) \n
    all_sprites: pygame group of sprites object \n
    pipes: pygame group of sprites object (pipes only) \n
    tick_count: int \n
    score: int \n
    Methods
    -------
    new()
        Initialize new game.
    reset()
        Reset game to blank state.
    run()
        Mainloop of game.
    scroll_background()
        Makes background scroll.
    events()
        Managing game events.
    start_screen(permanent=True, file_ref=None)
        Draw of screen waiting for event to run game.
    dead_screen()
        Draw of screen waiting for reset game after dead.
    score_count()
        Draw of player's score.
    update()
        Main update funct of draw, events etc.
    quit()
        Quit the app.

    """
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
        """
        Function    : initialize new game \n
        Description : do important func and set vars before start of game \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.new()
        """
        self.reset()
        self.player = Player(self, 50, 400)
        self.all_sprites.add(self.player)
        self.screen.blit(pg.transform.scale(
            BACKGROUND, (WIDTH, HEIGHT)), (0, 0))
        self.draw_base()

    def reset(self):
        """
        Function    : reset game to blank state \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.reset()
        """
        self.all_sprites.empty()
        self.player = None
        self.score = 0
        self.pipes.empty()

    def run(self):
        """
        Function    : mainloop of game \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.run()
        """
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
            self.scroll_background(x, BACKGROUND)
            self.draw_base()
            self.update()
            x -= 1

    def scroll_background(self, x: int, image: object):
        """
        Function    : makes background scroll \n
        Parameters  : self, x: int (count), image: pygame Image object\n
        Return      : None \n
        Examples of Usage: self.scroll_background(x: int)
        """
        rel_x = x % self.screen.get_rect().width
        self.screen.blit(pg.transform.scale(
            image, (WIDTH, HEIGHT)), (rel_x - self.screen.get_rect().width, 0))

        if rel_x < WIDTH:
            self.screen.blit(pg.transform.scale(
                image, (WIDTH, HEIGHT)), (rel_x, 0))

    def events(self):
        """
        Function    : managing events \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.events()
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def start_screen(self):
        """
        Function    : draw of screen waiting for event to run game \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.start_screen()
        """
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
        """
        Function    : draw of screen waiting for reset game after dead \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.dead_screen()
        """
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
        """
        Function    : draw of player's score \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.score_count()
        """
        score_text = self.font.render(
            f"Score: {str(int(self.score /2))}", True, (255, 255, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (200 // 2, 60 // 2)
        self.screen.blit(score_text, score_text_rect)

    def draw_base(self):
        """
        Function    : draw of base image \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.draw_base()
        """
        self.screen.blit(pg.transform.scale(
            BASE, (WIDTH, BASE.get_height())), (0, HEIGHT - BASE.get_height()))

    def update(self):
        """
        Function    : main update function \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.update()
        """
        self.all_sprites.draw(self.screen)
        self.pipes.draw(self.screen)
        self.draw_base()
        self.pipes.update()
        self.player.update()
        self.score_count()
        pg.display.update()

    def quit(self):
        """
        Function    : quit the game \n
        Parameters  : self \n
        Return      : None \n
        Examples of Usage: self.quit()
        """
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
