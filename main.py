import pygame
from checkers.constants import WIDTH, HEIGHT, FPS
from checkers.board import Board

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()


    while run:
        #making sure we have 60 fps
        clock.tick(FPS)

        # basic event loop (check to see if any even happend)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

main()
