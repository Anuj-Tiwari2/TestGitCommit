from PieceType import *

"""
Piece Class encapsulates information about a piece
"""
class Piece():
    """
    An abstract piece on a board has a type and position
    - Specific classes based on types have 
        - specific positions
        - moves (self.moves)
        - count of moves (self.moveCount)
        - move directions (self.moveDir)
    """
    def __init__(self, pieceType, position):
        self.pieceType = pieceType
        self.position = (position[0], position[1])

    def _validDim(self, dim):
        return dim>0 and dim<9

    def getValidPos(self, piece_dir, cord, visited):
        new_cord = (piece_dir[0]+cord[0], piece_dir[1]+cord[1])
        if( self._validDim(new_cord[0])
            and self._validDim(new_cord[1])
            and not visited[new_cord[0]-1][new_cord[1]-1]):
            return new_cord
        return None

    def getPositionNums(self):
        return (ord(self.position[0])-ord('A')+1,ord(self.position[1])-ord('0'))
    
    def getPieceType(self):
        return self.pieceType

    def getMoves(self, startPos, my_moves, visit_board):
        self.moveCount = self.moveCount-1
        while(self.moveCount>=0):
            for piece_dir in self.moveDir:
                move = self.getValidPos(piece_dir, startPos, visit_board)
                if(move is not None ):
                    my_moves.append( move )
                    # board matrix is indexed 0-7,
                    # aligning to 1-8
                    visit_board[move[0]-1][move[1]-1] = 1
                    self.getMoves(move, my_moves, visit_board)

class King(Piece):
    def __init__(self, position):
        super().__init__(PieceType.King, position)
        self.moveDir = [
                        (-1, -1), (-1, 0), (-1,1),
                        (0, 1),(0,-1),
                        (1, -1), (1, 0), (1, 1)
                    ]
        self.moveCount = 1

class Queen(Piece):
    def __init__(self, position):
        super().__init__(PieceType.Queen, position)
        self.moveDir = [   
                        (-1, -1), (-1, 0), (-1,1),
                        (0, 1),(0,-1),
                        (1, -1), (1, 0), (1, 1)
                    ]
        self.moveCount = 8

class Knight(Piece):
    def __init__(self, position):
        super().__init__(PieceType.Knight, position)
        self.moveDir = [(-2, -1), (-2, 1),
                        (-1, -2), (-1, 2),
                        (1, -2), (1, 2),
                        (2, -1), (2, 1),
                        ]
        self.moveCount = 1

class Rook(Piece):
    def __init__(self, position):
        super().__init__(PieceType.Rook, position)
        self.moveDir = [
            (1,0), (0,1)
        ]
        self.moveCount = 8

class Bishop(Piece):
    def __init__(self, position):
        super().__init__(PieceType.Bishop, position)
        self.moveDir = [
            (-1, -1), (-1,1),
            (1, -1), (1,1) 
        ]
        self.moveCount = 8

class Pawn(Piece):
    def __init__(self, position):
        super().__init__(PieceType.Pawn, position)
        self.moveDir = [
            (1,0), (0,1), (1, 1), (1,-1)
        ]
        self.moveCount = 1