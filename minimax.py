#1.Pahile board banaun gheycha,print krun bghycha
#2.check krycha winner(boolean mdhe jr board[a]==board[b]==board[c] then true)
#3.Full ahe ka bghych  return " " not in board
#4.minimax function with parameter is_maximizing function....if check_winner("X")...
#5.is_maximizing function
#6.computer_move function
#7.main function

n=3
board=[" "]*(n*n)
def print_board():
  print(f"""
       {board[0]} |{board[1]} |{board[2]}
        -------
       {board[3]} |{board[4]} |{board[5]}
        -------
       {board[6]} |{board[7]} |{board[8]}
        """)
print_board()
def check_winner(player):
  wins = [(0,1,2), (3,4,5), (6,7,8),  # Rows
            (0,3,6), (1,4,7), (2,5,8),  # Columns
            (0,4,8), (2,4,6)]     #diagonals
  for a,b,c in wins:
    if board[a]==board[b]==board[c]==player:
      return True
  return False


def is_board_full():
    return " " not in board

def minimax(is_maximizing):
    # If computer wins, return +1
    if check_winner("O"):
        return 1
    # If player wins, return -1    
    if check_winner("X"):
        return -1
    # If draw, return 0    
    if is_board_full():
        return 0
        
    if is_maximizing:
        best_score = -1000
        # Try all spaces
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"  # Try move
                score = minimax(False)  # Check opponent's move
                board[i] = " "  # Undo move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        # Try all spaces
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"  # Try move
                score = minimax(True)  # Check opponent's move
                board[i] = " "  # Undo move
                best_score = min(score, best_score)
        return best_score

def computer_move():
    best_score = -1000
    best_move = 0
    # Try all spaces
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"  # Try move
            score = minimax(False)  # Check opponent's move
            board[i] = " "  # Undo move
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"  # Make the best move

def main():
    print("Positions are numbered 0-8, like this:")
    print("0 | 1 | 2\n---------\n3 | 4 | 5\n---------\n6 | 7 | 8")
    
    while True:
        print_board()
        
        # Player's turn
        move = int(input("Enter your move (0-8): "))
        if board[move] != " ":
            print("That space is taken! Try again.")
            continue
        board[move] = "X"
        
        # Check if player won
        if check_winner("X"):
            print_board()
            print("You win!")
            break
            
        # Check for draw
        if is_board_full():
            print_board()
            print("It's a draw!")
            break
            
        # Computer's turn
        print("Computer is thinking...")
        computer_move()
        
        # Check if computer won
        if check_winner("O"):
            print_board()
            print("Computer wins!")
            break

# Start the game
main()