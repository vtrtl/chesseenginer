import tkinter as tk

tile_size = 64

class ChessBoard():
    def __init__(self,board):
        self.board = board
        self.window = tk.Tk()
        self.canvas = tk.Canvas(self.window, width=tile_size*8, height=tile_size*8)
        self.canvas.pack()


    def drawboard(self):
        colors = ["#000000", "#FFFFFF"]
        for r in range(8):
            for c in range(8):
                color = colors[((r+c) % 2)]
                x1 = c * tile_size
                y1 = r * tile_size
                x2 = x1 + tile_size
                y2 = y1 + tile_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                piece = self.board.board[r][c]
                if piece != "--":
                    self.drawpiece(piece, r, c)

    def drawpieces(self): 
        for c in range(8):
            for r in range(8):
                piece = self.board.board[r][c]
                if piece != "--":
                    x = c * tile_size + tile_size // 2
                    y = r * tile_size + tile_size // 2
                    self.canvas.create_text(x, y, text=piece, font=("Arial", 24), fill="red")

    def drawpiece(self, piece, r, c):
        x = c * tile_size + tile_size // 2
        y = r * tile_size + tile_size // 2
        self.canvas.create_text(x, y, text=piece, font=("Arial", 24), fill="red")

    def start(self):
        self.drawboard()
        self.window.mainloop()