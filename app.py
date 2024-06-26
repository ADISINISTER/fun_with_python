from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Game variables
PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "
BOARD_SIZE = 3

# Create the game board
board = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Variables
current_player = PLAYER_X
moves = 0

@app.route('/')
def index():
    return render_template('index.html', board=board, current_player=current_player)

@app.route('/make_move', methods=['POST'])
def make_move():
    global current_player, moves

    row = int(request.form['row'])
    col = int(request.form['col'])

    if board[row][col] == EMPTY:
        # Update the board
        board[row][col] = current_player

        # Check for a win or a tie
        if check_winner(current_player):
            return redirect('/game_over')
        elif moves == BOARD_SIZE ** 2 - 1:
            return redirect('/game_over')

        # Switch players
        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X
        moves += 1

    return redirect('/')

@app.route('/game_over')
def game_over():
    return render_template('game_over.html', winner=current_player)

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

if __name__ == '__main__':
    app.run(debug=True)
