from classes.board import Board
from classes.piece import Piece
from classes.pieces.bishop import Bishop
from classes.pieces.queen import Queen
from classes.pieces.rook import Rook
from classes.pieces.knight import Knight
from classes.pieces.pawn import Pawn

from pprint import pprint

from classes.team import Team

board = Board()

# These pieces are done!
bishop = Piece(board, 5, 5, Bishop, Team(Team.WHITE))
rook = Piece(board, 5, 4, Rook, Team(Team.BLACK))
queen = Piece(board, 4, 4, Queen, Team(Team.BLACK))
knight = Piece(board, 3, 3, Knight, Team(Team.BLACK))
pawn = Piece(board, 4, 6, Pawn, Team(Team.BLACK))

pawn.logic.first_move = False
# print(bsh, id(bsh))

# print(f"{id(board)=}, {id(bsh.board)=} | {id(board)==id(bsh.board)}")
# print(board.board[0][0])
print(pawn.logic.get_available_moves())
pprint(board.board, width=300)