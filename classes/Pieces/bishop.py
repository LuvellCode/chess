# слон
from .base_logic import BaseLogic

class Bishop(BaseLogic):
    
    def get_available_moves(self) -> list:
        """
        returns a set of moves for each diagonal direction
        """
        moves = []

        for dx in (-1, 1):
            for dy in (-1, 1):
                moves.extend(self.get_moves_based_on_direction(self.piece, dx, dy))

        return set(moves)

        # OLD VERSION:

        # x, y = starting_point
        # # moves -> bottom left (diagonal)
        # while x < max_x and y > min_y:
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
        #     y -= 1
        # print(f"+ bot l: {moves}")

        # x,y = starting_point
        # # moves -> top left (diagonal)
        # while x > min_x and y > min_y:
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
        #     y -= 1
        # print(f"+ top l: {moves}")

        # x,y = starting_point
        # # moves -> top right (diagonal)
        # while x > min_x and y < max_y:
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
        #     y += 1
        # print(f"+ top r: {moves}")

        # x,y = starting_point
        # # moves -> bot right (diagonal)
        # while x < max_x and y < max_y:
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
        #     y += 1
        # print(f"+ bot r: {moves}")


        # return set(moves)
