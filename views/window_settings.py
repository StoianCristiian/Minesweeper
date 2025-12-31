import tkinter as tk
from tkinter import messagebox
import constants

class WindowSettings(tk.Toplevel):
    def __init__(self, start_game_window):
        super().__init__()
        self.title("Setari joc")
        self.geometry("600x600")
        self.start_game_window = start_game_window

        tk.Label(self, text="Randuri = ").pack()
        self.game_rows = tk.Entry(self)
        self.game_rows.insert(0, str(constants.ROWS))
        self.game_rows.pack()

        tk.Label(self, text="Coloane = ").pack()
        self.game_cols = tk.Entry(self)
        self.game_cols.insert(0, str(constants.COLS))
        self.game_cols.pack()

        tk.Label(self, text="Mine = ").pack()
        self.game_mines = tk.Entry(self)
        self.game_mines.insert(0, str(constants.MINES))
        self.game_mines.pack()

        tk.Label(self, text="Secunde = ").pack()
        self.game_time = tk.Entry(self)
        self.game_time.insert(0, str(constants.TIME))
        self.game_time.pack()

        tk.Button(self, text="START", command=self.submit).pack(pady=10)

        self.protocol("WM_DELETE_WINDOW", self.close_window)


    def close_window(self):
        self.master.destroy()
        self.destroy()
        

    def submit(self):
        try:
            r=int(self.game_rows.get())
            c=int(self.game_cols.get())
            m=int(self.game_mines.get())
            s=int(self.game_time.get())

            if m >= r*c:
                messagebox.showerror("Eroare", "Prea multe mine")
                return
            
            self.start_game_window(r,c,m,s)
            self.destroy()
        except ValueError:
            messagebox.showerror("Eroare", "Introdu numere valide!")
        
