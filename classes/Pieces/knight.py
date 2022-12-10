# хорс, кінь

from itertools import product
from .base_logic import BaseLogic

class Knight(BaseLogic):
    
    def get_available_moves(self) -> list:
        """
        returns a set of moves ...
        """
        starting_point = self.piece.x, self.piece.y
        min_x, min_y = 0, 0
        max_x = max_y = self.piece.board.size

        moves = []
        x, y = starting_point

        # All Horse Movements: 
        moves_all = list(product([x-1, x+1],[y-2, y+2])) + list(product([x-2,x+2],[y-1,y+1]))
        
        # moves = [(x,y) for x,y in moves_all if x >= min_x and y >= min_y and x < max_x and y < max_y]
        for x,y in moves_all:
            other_piece = self.piece.board.get_piece_from_slot(x, y)
            if x >= min_x and y >= min_y and x < max_x and y < max_y:
                if other_piece is not None and not self.piece.can_beat(other_piece):
                    continue
                moves.append((x,y))
            

        return set(moves)
