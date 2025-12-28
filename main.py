from models import Board

if __name__ == '__main__':
    rows = 3
    cols = 5
    mines = 3

    board = Board(rows,cols,mines)
    board.grid[2][2].is_flagged = True
    for i in range(0,rows):
        for j in range(0, cols):
            print(f"{board.grid[i][j].neighbours_mines}-{board.grid[i][j].is_mine}-{board.grid[i][j].is_flagged}", end=' ')
        print()