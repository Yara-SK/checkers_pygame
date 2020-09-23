import pygame
from .constants import BLACK, RED, GREY, SQS, CROWN
class Piece:
    PADIING = 13
    BORDER = 4

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

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
        pygame.draw.circle(win,GREY,(self.x, self.y),radius+self.BORDER)
        pygame.draw.circle(win,self.color,(self.x, self.y),radius)
        if self.king:
            # drawing crown in the middle of the piece
            win.blit(CROWN, (self.x-CROWN.get_width()/2, self.y-CROWN.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    # to avoid <object at x2342....>
    def __repr__(self):
        return str(self.color)
