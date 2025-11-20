from engine.board import Board
from gui.window import ChessBoard
if __name__ == "__main__":
    chessboard = Board()
    gui = ChessBoard(chessboard)
    gui.drawpieces()
    gui.start()