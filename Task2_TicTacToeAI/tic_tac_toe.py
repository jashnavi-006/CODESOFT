import random

board = [" " for _ in range(9)]

# ---------------- BOARD ----------------
def print_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

# ---------------- PLAYER MOVE ----------------
def player_move():
    try:
        move = int(input("Enter position (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Invalid move! Choose 1-9.")
            return player_move()

        if board[move] == " ":
            board[move] = "X"
        else:
            print("Position already taken!")
            return player_move()

    except ValueError:
        print("Please enter a number!")
        return player_move()

# ---------------- CHECK WINNER ----------------
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# ---------------- DRAW ----------------
def is_draw():
    return " " not in board

# ---------------- EVALUATION ----------------
def evaluate():
    if check_winner("O"):
        return 1
    elif check_winner("X"):
        return -1
    else:
        return 0

# ---------------- MINIMAX ----------------
def minimax(is_maximizing):
    score = evaluate()

    if score == 1 or score == -1:
        return score

    if is_draw():
        return 0

    if is_maximizing:
        best = -1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                best = max(best, minimax(False))
                board[i] = " "
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                best = min(best, minimax(True))
                board[i] = " "
        return best

# ---------------- AI MOVE ----------------
def ai_move():
    best_score = -1000
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"

# ---------------- GAME LOOP ----------------
while True:
    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break