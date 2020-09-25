import pygame
from .board import Board
from .constants import RED, BLUE, WHITE, SQS

class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()

    def select(self,row,col):
        if self.selected: #piece selected
            result = self._move(row,col) #move to a certain square
            if not result: #if the move is illegal
                self.selected = None #reset the move
                self.select(row,col) #run the code after 'else'

        piece = self.board.get_piece(row,col)
        if piece != 0 and piece.color == self.turn:
        #if we're not selecting an empty piece and it's the color of turn
            self.selected = piece #
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
        #if we selected s/ and in (row,col) there is no other piece, and
        #if the square where we want to move the piece is valid_moves
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(
                    self.win,BLUE,(col*SQS + SQS//2, row*SQS + SQS//2),15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn == RED
