import pygame
from .constants import BLACK, RED, GRAY, SQS
class Piece:
    PADIING = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    # calculating the position of a round piece
    def calc_pos(self):
        self.x = SQS*self.col + SQS // 2
        self.y = SQS*self.row + SQS // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQS//2 - self.PADIING
        pygame.draw.circle(win,GRAY,self.color,(self.x, self.y),radiuss+self.OUTLINE)
        pygame.draw.circle(win,self.color,(self.x, self.y),radiu)

    # to avoid <object at x2342....>
    def __repr__(self):
        return str(self.color)
