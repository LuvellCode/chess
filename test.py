from classes.board import Board
from classes.Pieces.bishop import Bishop
from pprint import pprint

from classes.team import Team

board = Board()

bsh = Bishop(board, 0, 0, Team(Team.WHITE))
# print(bsh, id(bsh))

# print(f"{id(board)=}, {id(bsh.board)=} | {id(board)==id(bsh.board)}")
# print(board.board[0][0])
pprint(board.board, width=300)