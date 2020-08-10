from os import path
import pygame as pg

pg.mixer.init()
# DISPLAY SETTINGS
WIDTH = 600
HEIGHT = 800

# GAME SETTINGS
TITLE = "Flappy"
FPS = 60



# SOUNDS
DIE_SOUND = pg.mixer.Sound(path.join('assets/sounds','die.wav'))
JUMP_SOUND = pg.mixer.Sound(path.join('assets/sounds','wing.wav'))
POINT_SOUND = pg.mixer.Sound(path.join('assets/sounds','point.wav'))

# IMAGES
BIRD1 = pg.image.load(path.join('assets/images','bird1.png'))
BIRD2 = pg.image.load(path.join('assets/images','bird2.png'))
BIRD3 = pg.image.load(path.join('assets/images','bird3.png'))

BACKGROUND = pg.image.load(path.join('assets/images','bg.png'))
PIPE = pg.image.load(path.join('assets/images', 'pipe.png'))
BASE = pg.image.load(path.join('assets/images', 'base.png'))