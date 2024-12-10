import random

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    for _ in range(9):
        display_board(board)
        player = players[turn]
        print(f"Player {player}'s turn")

        if player == "X":  # Human player
            row, col = map(int, input("Enter row and column (0-2): ").split())
        else:  # Computer player
            row, col = random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == " "])

        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                return
            turn = 1 - turn
        else:
            print("Cell already occupied. Try again.")

    display_board(board)
    print("It's a draw!")

tic_tac_toe()