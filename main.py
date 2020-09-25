import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED, FPS
from checkers.board import Board
from checkers.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

# doing things with the mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y//SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        #making sure we have 60 fps
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())

        # basic event loop (check to see if any even happend)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)

        #board.draw_squares(WIN)
        game.update()

    pygame.quit()

main()
