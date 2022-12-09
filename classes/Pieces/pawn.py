# пішка

from .base_logic import BaseLogic
from ..team import Team

class Pawn(BaseLogic):

    def __init__(self, parent_piece) -> None:
        self.first_move = True
        super().__init__(parent_piece)
    
    def get_available_moves(self) -> list:
        """
        returns a set of moves ...
        """
        x, y = self.piece.x, self.piece.y
        min_x, min_y = 0, 0
        max_x = max_y = self.piece.board.size

        moves = []
        piece = self.piece
        board_matrix = piece.board.board
        
        team_coeff = self.get_team_coefficient()

        # so unclean. probably need to add this to the `base_logic.py` method
        # (add limits to the function)
        if self.first_move:
            for i in (1,2):
                new_x = x + team_coeff*i
                other_piece = board_matrix[new_x][y]
                if other_piece is not None:
                    break
                moves.append((new_x, y))
        else:
            new_x = x + team_coeff
            other_piece = board_matrix[new_x][y]
            if other_piece is None:
                moves.append((new_x, y))
        print(f"before check len == 0: {moves}")
        # if len == 0 then some piece is blocking the current pawn
        # x+1, y-1
        # x+1, y+1
        new_x = x + team_coeff
        new_y = y + 1
        other_piece = board_matrix[new_x][new_y]
        if other_piece is not None and self.piece.can_beat(other_piece):
            moves.append((new_x,new_y))
        print(moves)
        new_x = x + team_coeff
        new_y = y - 1
        other_piece = board_matrix[new_x][new_y]
        if other_piece is not None and self.piece.can_beat(other_piece):
            moves.append((new_x,new_y))
        print(moves)
        return set(moves)
    
    def get_team_coefficient(self):
        check = self.piece.team == Team(Team.BLACK)
        return 1 if check else -1
