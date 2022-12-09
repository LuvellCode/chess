# tower, тура

from .base_logic import BaseLogic

class Rook(BaseLogic):
    
    def get_available_moves(self) -> list:
        """
        returns a set of moves ...
        """
        moves = []

        for dx, dy in ((-1, 0), (1, 0), (0, 1), (0, -1)):
                moves.extend(self.get_diagonal_moves_based_on_direction(self.piece, dx, dy))

        return set(moves)

        # OLD VERSION
        # starting_point = self.piece.x, self.piece.y
        # min_x, min_y = 0, 0
        # max_x = max_y = self.piece.board.size

        # moves = []

        # x, y = starting_point
        # # moves -> left
        # while y > min_y:
        #     if x == starting_point[0] and y == starting_point[1]:
        #         pass
        #     else:
        #         other_piece = self.piece.board.board[x][y]
        #         if other_piece is not None:
        #             if self.piece.can_beat(other_piece):
        #                 moves.append((x,y))
        #             break
        #         moves.append((x,y))
        #     y -= 1
        # print(f"+left: {moves}")

        # x, y = starting_point
        # # moves -> right
        # while y < max_y:
        #     if x == starting_point[0] and y == starting_point[1]:
        #         pass
        #     else:
        #         other_piece = self.piece.board.board[x][y]
        #         if other_piece is not None:
        #             if self.piece.can_beat(other_piece):
        #                 moves.append((x,y))
        #             break
        #         moves.append((x,y))
        #     y += 1
        # print(f"+right: {moves}")
        
        # x, y = starting_point
        # # moves -> top
        # while x > min_x:
        #     if x == starting_point[0] and y == starting_point[1]:
        #         pass
        #     else:
        #         other_piece = self.piece.board.board[x][y]
        #         if other_piece is not None:
        #             if self.piece.can_beat(other_piece):
        #                 moves.append((x,y))
        #             break
        #         moves.append((x,y))
        #     x -= 1
        # print(f"+top: {moves}")

        # x, y = starting_point
        # # moves -> bottom
        # while x < max_x:
        #     if x == starting_point[0] and y == starting_point[1]:
        #         pass
        #     else:
        #         other_piece = self.piece.board.board[x][y]
        #         if other_piece is not None:
        #             if self.piece.can_beat(other_piece):
        #                 moves.append((x,y))
        #             break
        #         moves.append((x,y))
        #     x += 1
        # print(f"+bot: {moves}")

        # return set(moves)
