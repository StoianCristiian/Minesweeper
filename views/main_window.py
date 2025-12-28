import tkinter as tk
from tkinter import messagebox

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minesweeper typeshit")
        self.resizable(True, True)
        self.state("zoomed")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()