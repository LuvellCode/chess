# слон
from ..piece import Piece

class Bishop(Piece):
    
    def get_available_moves(self) -> list:
        """
        returns a set of moves for each diagonal direction
        """
        starting_point = self.x, self.y
        min_x, min_y = 0, 0
        max_x = max_y = self.board.size

        moves = []

        x, y = starting_point
        
        # moves -> bottom left (diagonal)
        while x < max_x and y > min_y:
            moves.append((x,y))
            if self.board[x][y] is not None:
                break
            x += 1
            y -= 1

        x,y = starting_point
        # moves -> top left (diagonal)
        while x > min_x and y > min_y:
            moves.append((x,y))
            if self.board[x][y] is not None:
                break
            x -= 1
            y -= 1
        
        # moves -> top right (diagonal)
        while x > min_x and y < max_y:
            moves.append((x,y))
            if self.board[x][y] is not None:
                break
            x -= 1
            y += 1
        
        # moves -> bot right (diagonal)
        while x < max_x and y < max_y:
            moves.append((x,y))
            if self.board[x][y] is not None:
                break
            x += 1
            y += 1

        return set(moves)
