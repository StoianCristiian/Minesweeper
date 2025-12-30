import tkinter as tk
from views import MainWindow, BoardView
from models import Board
# if __name__ == '__main__':
#     rows = 10
#     cols = 10
#     mines = 3

#     board = Board(rows,cols,mines)
#     board._cell_click_reveal_(2,2)
#     for i in range(0,rows):
#         for j in range(0, cols):
#             print(f"{board.grid[i][j].neighbours_mines}-{board.grid[i][j].is_mine}-{board.grid[i][j].is_revealed}", end=' ')
#         print()


def onClick(r, c):
    print(f"Click pe {r}, {c}")

if __name__ == "__main__":
    app = MainWindow()

    r=10
    c=10
    m=10
    test_board = Board(r, c, m)

    view = BoardView(app.board_container, r, c, onClick, onClick)
    
    app.mainloop()