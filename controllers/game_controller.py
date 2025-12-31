from models import Board
from views import MainWindow, BoardView, WindowSettings
import tkinter as tk

class GameController:
    def __init__(self):
        self.root_setup = tk.Tk()
        self.root_setup.withdraw()

        self.settings = WindowSettings(self.setup_game)
        self.root_setup.mainloop()

    
    def setup_game(self,r,c,m,t):
        self.rows = r
        self.cols = c
        self.mines = m
        self.time_remained = t
        self.timer_runs = False

        self.root_setup.destroy()

        self.board = Board(self.rows, self.cols, self.mines)
        self.root = MainWindow()
        self.board_table = BoardView(self.root.board_container, self.rows, self.cols, self.left_clk, self.right_clk)

        self.root.timerRunning(self.time_remained)
        self.root.mainloop()
        

    def start_time(self):
        if not self.timer_runs:
            self.timer_runs = True
            self.update_time()

    
    def update_time(self):
        if self.board.game_over:
            return

        if self.timer_runs and not self.board.game_over:
            self.time_remained -= 1
            self.root.timerRunning(self.time_remained)
            self.root.after(1000, self.update_time)
        
        if self.time_remained <= 0:
            self.timer_runs = False
            self.board.game_over = True
            self.root.showGameOver(won=2)


    def left_clk(self,r,c):
        if not self.timer_runs:
            self.start_time()

        if self.board.game_over:
            return
        
        all_cells_revealed = self.board._cell_click_reveal_(r,c)
        for cell in all_cells_revealed:
            self.board_table.update_button(cell.row, cell.column, cell)

        if self.board.game_over:
            self.showAllMines()
            self.timer_runs = False
            self.root.showGameOver(won=0)
        elif self.board.checkWin():
            self.board.game_over = True
            self.timer_runs = False
            self.root.showGameOver(won=1)




    def right_clk(self,r,c):
        if self.board.game_over:
            return
        
        cell = self.board._putFlag_(r,c)
        self.board_table.update_button(r,c,cell)



    def showAllMines(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.board.grid[r][c]
                if cell.is_mine:
                    cell.is_revealed = True
                    self.board_table.update_button(r,c,cell)



    def start_game(self):
        self.root.mainloop()
    