from Board import *
import json
import os


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_html')

@app.route('/chess/<r_piece>', methods=['POST', 'GET'])
def get_moves(r_piece):
    '''
    # request ={
        "positions":
        {
            "Queen":"E7",
            "Bishop":"B7",
            "Rook":"G5",
            "Knight":"C3"
        }
    }
    response  = {
        "valid_moves:['A4', 'A2', 'B1', 'D1']"
    }
    '''
    board = Board()
    with open(os.path.join(os.getcwd(), 'TestCases', 'input.json'), 'r') as f:
        pieces = json.load(f)
        piecePositions = pieces['positions']
        if(r_piece not in {pType.lower() for pType in piecePositions.keys()}):
            return {
                "valid_moves":"Piece not on Board"
            }
        board.update(piecePositions)
        return {
            "valid_moves":board.getValidMoves(r_piece)
        }

if __name__ =="__main__":
    app.run(debug=True, port=5000)