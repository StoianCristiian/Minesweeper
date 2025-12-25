from models import Board

if __name__ == '__main__':
    rows = 3
    cols = 5

    board = Board(rows,cols,3)
    for i in range(0,rows):
        for j in range(0, cols):
            print(board.grid[i][j].is_mine)
        print()