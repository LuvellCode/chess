from .classes.piece import Piece

"""
class ChessGame:
    attributes:
        board: - board 8x8

class Board:
    attrs:
        board: matrix 8x8 of Slots
        current_move: - id of the player to make a move

class Slot:
    x, y: - position (easier to manage)

class Figure:
    attrs:
        title = ""
    
    methods:
        move(): figure moving logic (eg., pawn - "l", horse - "Г" etc.). to be overloaded by child classes



"""


class ChessGame:
    def __init__(self):
        self.board = Board()