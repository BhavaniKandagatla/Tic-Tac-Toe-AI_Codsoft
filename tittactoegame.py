import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == player for cell in board[i]):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            row = int(input("Enter the row (1, 2, or 3): ")) - 1
            col = int(input("Enter the column (1, 2, or 3): ")) - 1
            if board[row][col] != " ":
                print("That cell is already taken. Try again.")
            else:
                return row, col
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 3.")

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game():
    board = [[" "]*3 for _ in range(3)]
    players = ["X", "0"]
    random.shuffle(players)
    print("Player", players[0], " AI goes first.")

    for turn in range(9):
        player = players[turn % 2]
        if player == "X":
            print("\nYour turn(Player X Turn):")
            row, col = player_move(board)
        else:
            print("\n AI turn(player 0 Turn):")
            row, col = ai_move(board)
        board[row][col] = player
        print_board(board)
        if check_winner(board, player):
            print(f"\nPlayer {player} wins!")
            return
    print("\nThe game is a draw.")

if __name__ == "__main__":
    play_game()
