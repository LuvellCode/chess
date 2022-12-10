
# Base logic class (to save the reference to Piece object so only logic class is updated as it's object attribute)
class BaseLogic:

    def __init__(self, parent_piece) -> None:
        self.piece = parent_piece

    def get_available_moves(self) -> list:
        """
        template. returns a set of moves ...
        """
        starting_point = self.piece.x, self.piece.y
        min_x, min_y = 0, 0
        max_x = max_y = self.piece.board.size

        moves = []

        return set(moves)

    @staticmethod
    def get_moves_based_on_direction(piece, dx:int, dy:int,*, min_range:int=1, max_range:int=0) -> list:
        """
        Used for bishop, queen, rook, pawn, king.
        Returns all clock directions (based on dx, dy)

        max_range: Limitation of max iterations, how close will the move range be;
        if max_range == 0 then the piece.board.size will be used.
        max_range: minimal radius of the moves to be located. E.g. for Knight it is 2 because it's moves are 2 indexes away from itself.

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
        # min_range = 1

        max_range = piece.board.size if max_range == 0 else max_range
        if not isinstance(max_range, int) or max_range < min_range:
            raise ValueError(f'Max range must be more or equeal to {min_range} (max_range >= {min_range}), {max_range} given.')
        
        board = piece.board
        
        x, y = piece.x, piece.y


        i = min_range
        result = []
        while True:
            if not (i <= max_range):
                break
            new_x = x + dx*i
            new_y = y + dy*i

            # Check whether new point is within borders
            if not board.point_belongs(new_x, new_y):
                break

            other_piece = board.get_piece_from_slot(new_x, new_y)
            if other_piece is not None:
                # If any other piece on the way of current one
                if piece.can_beat(other_piece):
                    # If teams are different
                    result.append((new_x, new_y))
                break
            result.append((new_x,new_y))
            
            i += 1
        return result