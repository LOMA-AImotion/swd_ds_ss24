"""
TicTacToe Utility functions
- to determine whether a board is a won state
- to print a board to the console
"""

def check_winner(board):
    # Überprüfe die Reihen
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return True
    
    # Überprüfe die Spalten
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return True
    
    # Überprüfe die Diagonalen
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return True
    
    return False

def print_board(board): 
    print("------------------")
    for row in board:
        print(" ".join([" " if r == "" else r for r in row]))
    print("==================")

if __name__ == "__main__":
    test_board = [["X", "O", ""],
                  ["X", "", "O"],
                  ["X", "O", "O"]]
    print_board(test_board)
    print("This board is won? ", check_winner(test_board))

