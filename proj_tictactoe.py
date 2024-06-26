import tkinter as tk
from tkinter import messagebox

# Constants
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "
BOARD_SIZE = 3

# Create the game board
board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Variables
current_player = PLAYER_X
moves = 0

def reset_game():
    global board, current_player, moves

    # Clear the board
    board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    # Reset variables
    current_player = PLAYER_X
    moves = 0

    # Clear all buttons
    for button in buttons:
        button.config(text=EMPTY, state=tk.NORMAL, bg="#ffffff")

    player_info.config(text=f"Current Player: {current_player}")

def make_move(row, col):
    global current_player, moves

    if board[row][col] == EMPTY:
        # Update the board
        board[row][col] = current_player

        # Update the button text
        buttons[row][col].config(text=current_player, state=tk.DISABLED, bg="#cccccc")

        # Check for a win or a tie
        if check_winner(current_player):
            highlight_winner_moves(current_player)
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        elif moves == BOARD_SIZE ** 2 - 1:
            messagebox.showinfo("Game Over", "It's a tie!")
            reset_game()
        else:
            # Switch players
            current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
            moves += 1
            player_info.config(text=f"Current Player: {current_player}")

def check_winner(player):
    # Check rows
    for row in range(BOARD_SIZE):
        if all(board[row][col] == player for col in range(BOARD_SIZE)):
            return True

    # Check columns
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        return True

    if all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        return True

    return False

def highlight_winner_moves(player):
    # Check rows
    for row in range(BOARD_SIZE):
        if all(board[row][col] == player for col in range(BOARD_SIZE)):
            for col in range(BOARD_SIZE):
                buttons[row][col].config(bg="#a0d2a0")

    # Check columns
    for col in range(BOARD_SIZE):
        if all(board[row][col] == player for row in range(BOARD_SIZE)):
            for row in range(BOARD_SIZE):
                buttons[row][col].config(bg="#a0d2a0")

    # Check diagonals
    if all(board[i][i] == player for i in range(BOARD_SIZE)):
        for i in range(BOARD_SIZE):
            buttons[i][i].config(bg="#a0d2a0")

    if all(board[i][BOARD_SIZE - i - 1] == player for i in range(BOARD_SIZE)):
        for i in range(BOARD_SIZE):
            buttons[i][BOARD_SIZE - i - 1].config(bg="#a0d2a0")

# Create a main window
window = tk.Tk()
window.title("Tic Tac Toe")
window.configure(bg="#f2f2f2")

# Create buttons
buttons = []
for row in range(BOARD_SIZE):
    button_row = []
    for col in range(BOARD_SIZE):
        button = tk.Button(window, text=EMPTY, width=8, height=4,
                           command=lambda r=row, c=col: make_move(r, c),
                           font=("Helvetica", 24, "bold"), bg="#ffffff", fg="#333333")
        button.grid(row=row, column=col, padx=5, pady=5)
        button_row.append(button)
    buttons.append(button_row)

# Create player info label
player_info = tk.Label(window, text=f"Current Player: {current_player}",
                       font=("Helvetica", 16), bg="#f2f2f2", fg="#333333")
player_info.grid(row=BOARD_SIZE, columnspan=BOARD_SIZE, padx=5, pady=10)

# Create a reset button
reset_button = tk.Button(window, text="Reset", command=reset_game,
                         font=("Helvetica", 14, "bold"), bg="#ffffff", fg="#333333")
reset_button.grid(row=BOARD_SIZE + 1, columnspan=BOARD_SIZE, padx=5, pady=10)

# Start the Tkinter event loop
window.mainloop()
