class Board():
    def __init__(self):
        self.board = [ 
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.whitetomove = True
        self.moveLog = []
    
    def makemove(self, move):
        self.board[move.startrow][move.startcol] = "--"
        self.board[move.endrow][move.endcol] = move.pieceMoved

        if move.ispawnpromotion:
            self.board[move.endrow][move.endcol] = move.pieceMoved[0] + "Q"

    def undomove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startrow][move.startcol] = move.pieceMoved
            self.board[move.endrow][move.endcol] = move.pieceCaptured
            self.whitetomove = not self.whitetomove
    
    def getvalidmoves(self):
        moves = self.getallpossiblemoves()
        legal_moves = []
        for move in moves:
            self.makemove(move)
            self.whitetomove = not self.whitetomove
            if not self.incheck():
                legal_moves.append(move)
            self.undomove()

    def incheck(self):
        king_row, king_col = self.findking(self.whitetomove)
        # think about logic here
        return False

    def findking(self):
        king = "wK" if self.whitetomove else "bK"
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                if self.board[r][c] == king:
                    return r, c
        return None
    
    def allowedmoves(self, r, c):
        piece = self.board[r][c]
        if piece[1] == "P":
            return self.getpawnmoves(r, c)
        elif piece[1] == "R":
            return self.getrookmoves(r, c)
        elif piece[1] == "N":
            return self.getknightmoves(r, c)
        elif piece[1] == "B":
            return self.getbishopmoves(r, c)
        elif piece[1] == "Q":
            return self.getqueenmoves(r, c)
        elif piece[1] == "K":
            return self.getkingmoves(r, c)
        return []
    
    # todo: implement moves for each piece