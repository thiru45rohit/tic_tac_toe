import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title("Tic Tac Toe")
window.configure(bg="#1f1f2e")
window.geometry("400x450")
window.resizable(False, False)
player = "X"
board = [["" for _ in range(3)] for _ in range(3)]
button_font = ("Helvetica", 24, "bold")
title_font = ("Helvetica", 20, "bold")
def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "":
            return True
    if board[0][0] == board[1][1] == board[2][2] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] != "":
        return True
    return False
def is_draw():
    for row in board:
        if "" in row:
            return False
    return True
def on_click(row, col):
    global player
    if board[row][col] == "":
        buttons[row][col].config(text=player, fg="#00ffff" if player == "X" else "#ff66cc")
        board[row][col] = player
        if check_winner():
            messagebox.showinfo("Game Over", f"Player {player} wins!")
            reset_game()
        elif is_draw():
            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()
        else:
            player = "O" if player == "X" else "X"
def reset_game():
    global player, board
    player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="")

title_label = tk.Label(window, text="Tic-Tac-Toe", font=title_font, bg="#1f1f2e", fg="#ffffff")
title_label.pack(pady=20)
frame = tk.Frame(window, bg="#1f1f2e")
frame.pack()
buttons = []
for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(
            frame, text="", width=5, height=2, font=button_font,
            bg="#33334d", fg="#ffffff", activebackground="#4d4d66",
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j, padx=10, pady=10)
        row.append(btn)
    buttons.append(row)
restart_btn = tk.Button(window, text="Restart Game", font=("Helvetica", 14),
                        command=reset_game, bg="#00cc99", fg="#fff",
                        activebackground="#00b386")
restart_btn.pack(pady=10)
window.mainloop()
