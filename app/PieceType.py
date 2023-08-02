from enum import Enum

class PieceType(Enum):
    King=1    # - Moves one square in any direction.
    Queen=2   # - Moves any number of squares diagonally, horizontally, or vertically.
    Rook=3    # - Moves any number of squares horizontally or vertically.
    Bishop=4  # - Moves any number of squares diagonally.
    Knight=5  # - Moves in an ‘L-shape,’ two squares in a straight direction, and then one square perpendicular to that.
    Pawn=6    # - Moves one square forward, but on its first move, it can move two squares forward. It captures diagonally one square forward.
