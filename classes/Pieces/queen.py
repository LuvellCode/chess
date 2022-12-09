# ферзь

from .base_logic import BaseLogic

class Queen(BaseLogic):
    
    def get_available_moves(self) -> list:
        """
        returns a set of moves ...
        """
        moves = []

        # (-1,-1), (-1,0), (-1,1)
        # (0, -1), (0, 1)
        # (1, -1). (1, 0), (1, 1)
        # (0, 0) should be excluded because nothing changes
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == dy == 0:
                    continue
                moves.extend(self.get_diagonal_moves_based_on_direction(self.piece, dx, dy))
        return set(moves)

        # OLD VERSION

        # # Rook moves set
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


        # Bishop movements set
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
