import pygame
from checkers.constants import WIDTH, HEIGHT, FPS, SQS
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

# doing things with the mouse
def get_row_col_from_mouse(pos):
    x, y = pos
    row = y//SQS
    col = x//SQS
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    piece = board.get_piece(0,1)
    #board.move(piece,4,3)

    while run:
        #making sure we have 60 fps
        clock.tick(FPS)

        # basic event loop (check to see if any even happend)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)
                board.move(piece, 4, 3)

        #board.draw_squares(WIN)
        board.draw(WIN)
        pygame.display.update()

    pygame.quit()

main()
