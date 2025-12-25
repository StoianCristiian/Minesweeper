from models import Board

if __name__ == '__main__':
    rows = 3
    cols = 5

    board = Board(rows,cols)
    print(f"Tabla are {board.rows} randuri si {board.cols} coloane")
    celula = board.grid[2][2]
    print(f"celula de pe pozitia 2-2 este mina: {celula.is_mine}")