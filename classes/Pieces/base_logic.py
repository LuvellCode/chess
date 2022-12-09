
# Base logic class (to save the reference to Piece object so only logic class is updated as it's object attribute)
class BaseLogic:

    def __init__(self, parent_piece) -> None:
        self.piece = parent_piece

    def get_available_moves(self) -> list:
        """
        returns a set of moves ...
        """
        starting_point = self.piece.x, self.piece.y
        min_x, min_y = 0, 0
        max_x = max_y = self.piece.board.size

        moves = []

        return set(moves)

    @staticmethod
    def get_moves_based_on_direction(piece, dx, dy):
        """
        Used for bishop, queen, rook.
        Returns all clock directions (based on dx, dy)

        Possible dx, dy pairs : direction
         0, -1 : left
        -1, -1 : top left
        -1,  0 : top
        -1,  1 : top right
         1,  0 : right
         1,  1 : bot right
         0,  1 : bot
         1, -1 : bot left
         
        """
        
        board_matrix = piece.board.board
        min_x, min_y = 0, 0
        max_x = max_y = piece.board.size
        
        x, y = piece.x, piece.y

        i = 1
        result = []
        while True:
            new_x = x + dx*i
            new_y = y + dy*i

            if min_x <= new_x < max_x and min_y <= new_y < max_y:
                other_piece = board_matrix[new_x][new_y]
                if other_piece is not None:
                    if piece.can_beat(other_piece):
                        result.append((new_x, new_y))
                    break
                result.append((new_x,new_y))
            else: 
                break
            i += 1
        return result