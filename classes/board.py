from .piece import Piece
from .Pieces.bishop import Bishop

class Board:
    # BLACK
    #   a b c d e f g h
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # WHITE
    def __init__(self, size=8) -> None:
        self.board = [[None for _ in range(size)] for _ in range(size)]
        self.size = size
        self.generate()

    def refresh(self):
        # Refreshes the position of each figure on the board
        self.generate()

        # ... Add the logic to place all the figures at their places
        pass
    
    def generate(self):
        """ 
        Clears all the slots. Init from Piece overwrites the values from board matrix
        
        """
        [[Piece(self, i, j) for j in range(self.size)] for i in range(self.size)]
        return self
    
    def default_setup(self):
        """
        Setup all the pieces to their slots
        """
        pass

    def get_piece_from_slot(self, x, y) -> Piece:
        """
        returns a piece at given coordinates
        """
        return filter(self.board, lambda slot: slot.x == x and slot.y == y)[0].piece

    def set_piece_to_slot(self, piece:Piece, x, y) -> None:
        """
        self-explanatory.
        """
        self.board[x][y].piece = piece

    def move_piece(self, piece:Piece, x:int, y:int):
        pass