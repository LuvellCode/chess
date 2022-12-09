# король

from .base_logic import BaseLogic

class King(BaseLogic):
    
    def get_available_moves(self) -> list:
        """
        returns a set of moves ...
        """
        starting_point = self.piece.x, self.piece.y
        min_x, min_y = 0, 0
        max_x = max_y = self.piece.board.size

        moves = []

        return set(moves)
