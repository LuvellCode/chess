from .piece import Piece
from .pieces.bishop import Bishop

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
    def __init__(self, size:int=8) -> None:
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
        Clears all the slots.
        NOTE: Piece.__init__ overwrites the values from board matrix
        
        """
        # [[Piece(self, i, j) for j in range(self.size)] for i in range(self.size)]
        return self
    
    def default_setup(self):
        """
        Setup all the pieces to their slots
        """
        # self.board[0][0]
        pass
    
    def point_belongs(self, x:int, y:int) -> bool:
        min_x, min_y = 0, 0
        max_x = max_y = self.size
        return min_x <= x < max_x and min_y <= x < max_y

    def get_piece_from_slot(self, x:int, y:int) -> Piece or None:
        """
        returns a piece at given coordinates
        """
        return self.board[x][y]

    def set_piece_to_slot(self, piece:Piece, x:int, y:int) -> None:
        """
        self-explanatory
        """
        self.board[x][y].piece = piece

    def move_piece(self, from_x:int, from_y:int, to_x:int, to_y:int):
        pass
    
    def piece_exists_at_slot(self, x,y) -> bool:
        return self.get_piece_from_slot(x,y) is not None
