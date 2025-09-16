import tkinter as tk
from tkinter import messagebox

current_player = "X"

def new_game():
    global current_player
    current_player = "X"
    for i in range(9):
        buttons[i].config(text=" ", state="normal", bg="white")

def check_winner():
    wins = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in wins:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != " ":
            buttons[a].config(bg="lightgreen")
            buttons[b].config(bg="lightgreen")
            buttons[c].config(bg="lightgreen")
            return buttons[a]["text"]
    if all(buttons[i]["text"] != " " for i in range(9)):
        return "Draw"
    return None

def on_click(i):
    global current_player
    if buttons[i]["text"] == " ":
        buttons[i].config(text=current_player, state="disabled")
        winner = check_winner()
        if winner:
            if winner == "Draw":
                messagebox.showinfo("Result", "It's a draw!")
            else:
                messagebox.showinfo("Result", f"Player {winner} wins! 🎉")
            new_game()
        else:
            current_player = "O" if current_player == "X" else "X"

root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg="skyblue")

title = tk.Label(root, text="Tic Tac Toe Game", font=("Arial", 20, "bold"), bg="skyblue", fg="darkblue")
title.grid(row=0, column=0, columnspan=3, pady=10)

buttons = []
for i in range(9):
    b = tk.Button(root, text=" ", font=("Arial", 24, "bold"), width=5, height=2,
                  bg="white", fg="black", command=lambda i=i: on_click(i))
    b.grid(row=(i//3)+1, column=i%3, padx=5, pady=5)
    buttons.append(b)

reset_button = tk.Button(root, text="New Game", font=("Arial", 14, "bold"),
                         bg="orange", fg="white", command=new_game)
reset_button.grid(row=4, column=0, columnspan=3, sticky="nsew", pady=10)

root.mainloop()
