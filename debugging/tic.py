#!/usr/bin/python3

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def print_winner_message(player):
    print("Player " + player + " wins!")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves_count = 0
    max_moves = 9

    while not check_winner(board) and moves_count < max_moves:
        print_board(board)

        while True:
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))

                if row not in [0, 1, 2] or col not in [0, 1, 2]:
                    print("Invalid input! Row and column must be 0, 1, or 2. Try again.")
                    continue

                if board[row][col] != " ":
                    print("That spot is already taken! Try again.")
                    continue

                board[row][col] = player
                moves_count += 1
                break
            except ValueError:
                print("Invalid input! Please enter an integer. Try again.")
        
        if check_winner(board):
            print_board(board)
            print_winner_message(player)
            break

        if moves_count >= max_moves:
            print_board(board)
            print("The game is a tie!")
            break

        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
