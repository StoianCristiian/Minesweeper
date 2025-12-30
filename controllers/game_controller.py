from models import Board
from views import MainWindow, BoardView
class GameController:
    def __init__(self):
        self.rows = 10
        self.cols = 10
        self.mines = 10

        self.board = Board(self.rows,self.cols,self.mines)
        self.root = MainWindow()
        self.board_table = BoardView(self.root.board_container,
                                     self.rows,
                                     self.cols,
                                     self.left_clk,
                                     self.right_clk,
                                     )
        
    def left_clk(self,r,c):
        if self.board.game_over:
            return
        
        all_cells_revealed = self.board._cell_click_reveal_(r,c)

        for cell in all_cells_revealed:
            self.board_table.update_button(cell.row, cell.column, cell)

    def right_clk(self,r,c):
        if self.board.game_over:
            return
        
        cell = self.board._putFlag_(r,c)
        self.board_table.update_button(r,c,cell)

    def start_game(self):
        self.root.mainloop()
    