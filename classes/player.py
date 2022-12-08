from .team import Team


class Player:
    def __init__(self, player_team:int) -> None:
        """
        player_team: Value from enum Team
        """
        self.player_team:int = player_team