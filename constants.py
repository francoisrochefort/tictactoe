import pygame
import os

# Alpha Beta pruning
MINFINITY = -1000
MAXFINITY = 1000

# board size
COLS = 3
ROWS = 3

# all possible player indexes
X = 0
O = 1

#
WIDTH: int = 500
HEIGHT: int = 500
HEIGHT_tot: int = 500
XO_WIDTH: int = 75
XO_HEIGHT: int = 50

FPS = 60
BACK_GROUND = pygame.image.load(os.path.join('Assets', 'space.png'))
YELLOW_O_IMAGE = pygame.image.load(os.path.join('Assets', 'o_modified-100x100.png'))
YELLOW_O = pygame.transform.rotate(pygame.transform.scale(
    YELLOW_O_IMAGE, (XO_WIDTH, XO_HEIGHT)), 0)
# YELLOW_O = pygame.image.load(os.path.join('Assets', 'zero.png'))

RED_X_IMAGE = pygame.image.load(os.path.join('Assets', 'X_modified-100x100.png'))
RED_X = pygame.transform.rotate(pygame.transform.scale(
    RED_X_IMAGE, (XO_WIDTH, XO_HEIGHT)), 0)

# SPACE = pygame.transform.scale(pygame.image.load(
#     os.path.join('Assets', 'space.png')), (WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# La position de l''image en haut en gauche
POSITIONS = [[40, 50], [225, 50], [400, 50],
             [40, 225], [225, 225], [400, 225],
             [40, 400], [225, 400], [400, 400]]
