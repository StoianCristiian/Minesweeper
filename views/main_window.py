import tkinter as tk
from tkinter import messagebox
from views import BoardView

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Minesweeper typeshit")
        self.state("zoomed")

        self.board_container = tk.Frame(self, relief=tk.SUNKEN, borderwidth=2)
        self.board_container.pack(padx=10, pady=10, expand=True, fill="both")

        self.header = tk.Frame(self)
        self.header.pack(pady=10)

        self.timer = tk.Label(self.header, text="Timp: 0", font=("Arial", 14, "bold"))
        self.timer.pack(side=tk.LEFT, padx=20)

    
    def showGameOver(self, won=False):
        if won == True:
            title = "Esti boss"
            message = "Ai gasit toate minele"
        else:
            title = "Slab"
            message = "ai lovit o mina"
        
        messagebox.showinfo(title, message)

