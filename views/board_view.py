import tkinter as tk

class BoardView:
    def __init__(self, master, rows, cols, left_clk, right_clk):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.buttons = []

        for r in range(rows):
            r_btns = []
            for c in range(cols):
                btn = tk.Button(
                    master,
                    width=3,
                    height=1,
                    font=("Arial", 10, "bold"),

                    command= lambda r=r, c=c: left_clk(r, c)
                )
            
                btn.bind("<Button-3>", lambda event, r=r, c=c: right_clk(r,c))

                btn.grid(row=r, column=c, sticky="nsew")
                r_btns.append(r_btns)
            self.buttons.append(r_btns)
