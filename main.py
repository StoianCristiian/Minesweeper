from models import Board

if __name__ == '__main__':
    rows = 10
    cols = 10
    mines = 3

    board = Board(rows,cols,mines)
    board._cell_click_reveal_(2,2)
    for i in range(0,rows):
        for j in range(0, cols):
            print(f"{board.grid[i][j].neighbours_mines}-{board.grid[i][j].is_mine}-{board.grid[i][j].is_revealed}", end=' ')
        print()