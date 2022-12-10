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

        # By default max_range = -1 to raise an exception if something goes wrong
        max_range = -1
        if self.first_move:
            max_range = 2
            # OLD Version
            # for i in (1,2):
            #     new_x = x + team_coeff*i
            #     other_piece = board_matrix[new_x][y]
            #     if other_piece is not None:
            #         break
            #     moves.append((new_x, y))
        else:
            max_range = 1
            # new_x = x + team_coeff
            # other_piece = board_matrix[new_x][y]
            # if other_piece is None:
            #     moves.append((new_x, y))
        moves.extend(self.get_moves_based_on_direction(piece, team_coeff, 0, max_range=max_range))

        print(f"after basic move forward check: {moves}")
        # if len == 0 then some piece is blocking the current pawn
        # x+1, y-1
        # x+1, y+1

        for dx,dy in ((team_coeff, 1), (team_coeff, -1)):
            generated_move = self.get_moves_based_on_direction(piece, dx, dy, max_range=1)
            print(f"Generated: {generated_move}")
            for new_x, new_y in generated_move:

                # if there is no piece then remove the move. 
                # Pawn can move diagonally only if there is any piece
                if not self.piece.board.piece_exists_at_slot(new_x, new_y):
                    generated_move.remove((new_x, new_y))
            print(f"Updated: {generated_move}")
            moves.extend(generated_move)
        # OLD VERSION
        # new_x = x + team_coeff*1
        # new_y = y + 1
        # other_piece = board_matrix[new_x][new_y]
        # if other_piece is not None and self.piece.can_beat(other_piece):
        #     moves.append((new_x,new_y))
        # print(moves)
        # new_x = x + team_coeff*1
        # new_y = y - 1
        # other_piece = board_matrix[new_x][new_y]
        # if other_piece is not None and self.piece.can_beat(other_piece):
        #     moves.append((new_x,new_y))
        print(moves)
        return set(moves)
    
    def get_team_coefficient(self):
        check = self.piece.team == Team(Team.BLACK)
        return 1 if check else -1
