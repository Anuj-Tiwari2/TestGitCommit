from Piece import *
from PieceType import *

"""
Board Class encapsulates information about a board
Board can have multiple pieces
"""
class Board():
    """
    On a board we have 
    - X Co-ordinate dimensions
    - Y Co-ordinate dimensions
    - list of pieces
    """
    class XCoord(object):
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                xCoords = []
                for i in range(0, 8):
                    xCoords.append('A'+str(i))
                return xCoords
            return xCoords

    class YCoord(object):
        def __new__(cls):
            if not hasattr(cls, 'instance'):
                yCoords = []
                for i in range(0, 8):
                    yCoords.append(str(i))
                return yCoords
            return yCoords
    
    def __init__(self):
        self.xCoords = Board.XCoord()
        self.yCoords = Board.YCoord()
        self.pieces  = []

    def getBoardLayout(self):
        return (self.xCoords, self.yCoords)

    def update(self, pieces):
        self.pieces = [ Piece( p_type, p_pos ) for p_type, p_pos in pieces.items() ]

    def filterMoves(self, piece, moves):
        # filter moves based on other pieces on board
        moves = moves - list(piece.getPositionNums())

    def getValidMoves(self, my_piece):
        pieceClassMap = {
            "king":King,
            "queen":Queen,
            "rook":Rook,
            "bishop":Bishop,
            "knight":Knight,
            "pawn":Pawn
        }
        try:
            visit_board = [
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]
            ]
            moves = []
            for piece in self.pieces:
                if(piece.pieceType.lower() == my_piece):
                    new_piece = pieceClassMap[my_piece](piece.position)
                    my_moves = []
                    new_piece.getMoves(piece.getPositionNums(), my_moves, visit_board)
            # for piece in self.pieces:
            #     self.filterMoves(self, piece, moves)
            return my_moves
        except Exception as e:
            raise Exception("Piece not valid on board - " +str(e))