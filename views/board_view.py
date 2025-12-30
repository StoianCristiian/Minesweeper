import tkinter as tk

class BoardView:
    def __init__(self, master, rows, cols, left_clk, right_clk):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.buttons = []

        for r in range(rows):
            self.master.rowconfigure(r, weight=1)
        for c in range(cols):
            self.master.columnconfigure(c, weight=1)

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
                r_btns.append(btn)
            self.buttons.append(r_btns)

    def update_button(self,r,c,cell):
        buton = self.buttons[r][c]

        if cell.is_revealed:
            buton.config(relief=tk.SUNKEN, bg="#e0e0e0")
            if cell.is_mine:
                buton.config(text="💣", bg="red")
            elif cell.neighbours_mines > 0:
                colors = {1: "blue", 2:"green", 3:"red", 4:"darkblue"}
                color = colors.get(cell.neighbours_mines, "black")
                buton.config(text=str(cell.neighbours_mines), fg=color)
            else:
                buton.config(text="")
        else:
            if cell.is_flagged:
                buton.config(text="🚩", fg="red")
            else:
                buton.config(text="", bg="SystemButtonFace")
