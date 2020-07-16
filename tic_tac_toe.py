class Player():
    def __init__(self, game_piece, name):
        self.game_piece = game_piece
        self.name = name

class Move():
    def __init__(self, author, postion):
        self.author = author
        self.postion = postion

class Board():
    moves = []

    def display(self):
        pass

    def add_move(self):
        pass

class Game():
    def __init__(self, board, p1, p2):
        self.board = board
        self.p1 = p1
        self.p2 = p2