import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("320x380")

player = "X"
board = [""] * 9

def check_winner():
    wins = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            messagebox.showinfo("Winner", f"Player {board[a]} Wins!")
            reset()
            return

    if "" not in board:
        messagebox.showinfo("Draw", "Match Draw!")
        reset()

def click(i):
    global player

    if board[i] == "":
        board[i] = player
        buttons[i]["text"] = player

        check_winner()

        player = "O" if player == "X" else "X"

def reset():
    global board, player
    board = [""] * 9
    player = "X"

    for b in buttons:
        b["text"] = ""

buttons = []

for i in range(9):
    btn = tk.Button(root,
                    text="",
                    font=("Arial",25),
                    width=5,
                    height=2,
                    command=lambda i=i: click(i))
    btn.grid(row=i//3,column=i%3)
    buttons.append(btn)

restart = tk.Button(root,
                    text="Restart",
                    font=("Arial",15),
                    command=reset)

restart.grid(row=4,column=0,columnspan=3,sticky="we")

root.mainloop()