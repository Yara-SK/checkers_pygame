import pygame

WIDTH = 800
HEIGHT = 800

ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS

#RGB
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

FPS = 60

#CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44,25))
CROWN = pygame.image.load('assets/crown.png')
CROWN = pygame.transform.scale(CROWN, (44,25))
