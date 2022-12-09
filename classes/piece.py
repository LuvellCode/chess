from classes.team import Team
from classes.pieces.base_logic import BaseLogic

class Piece:
    def __init__(self, board_parent, x:int, y:int, logic_class:BaseLogic=None, team:Team=None) -> None:
        """
        logic_class: BaseLogic, to save the reference to Piece object so only logic object may be updated as Piece's object attribute. 
        Useful for cases when the pawn gets to the end of the board, or game is being reset. 
        Reference for such cases will remain the same.
        """
        self.board = board_parent
        self.x:int = x
        self.y:int = y

        self.logic:BaseLogic = logic_class(self) if logic_class is not None else None

        self.is_alive:bool = True  # Needed for further implementations (eg. storing the defeated pieces etc.)

        self.board.board[self.x][self.y] = self
        self.team:Team = team  # Team Enum WHITE or BLACK
    
    def can_beat(self, other_piece):
        """
        checks whether current piece can beat the given one
        """
        return self.team != other_piece.team


    def __repr__(self) -> str:
        classname = f'{self.logic.__class__.__name__} ' if self.logic is not None else ''
        team_string = f', {self.team.name}' if self.team is not None else ''
        return f"<{classname}({self.x}, {self.y}{team_string})>"

    