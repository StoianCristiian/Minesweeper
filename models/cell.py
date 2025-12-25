class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.is_mine = False
        self.is_revealed = False
        self.is_flagged = False
        self.neighbours_mines = 0