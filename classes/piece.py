from classes.team import Team

class Piece:
    def __init__(self, board_parent, x:int, y:int, team: Team=None) -> None:
        self.board = board_parent
        self.x:int = x
        self.y:int = y
        self.is_alive:bool = True  # Needed for further implementations (eg. storing the defeated figures)
        self.board.board[self.x][self.y] = self
        self.team:Team = team  # Team Enum WHITE or BLACK

    def get_available_moves(self) -> list:
        """
        returns a list of available moves for piece. TO BE OVERRIDEN
        """
        pass

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} ({self.x}, {self.y}, {f'{self.team.name}' if self.team is not None else ''})>"

    