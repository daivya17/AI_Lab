import math

def print_board(board):
    """Prints the current state of the game board."""
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('| ' + ' | '.join(row) + ' |')

def available_moves(board):
    """Returns a list of available spots on the board."""
    return [i for i, spot in enumerate(board) if spot == ' ']

def check_winner(board, player):
    """Checks if the given player has won the game."""
    # Check for winning rows
    for i in range(0, 9, 3):
        if all(s == player for s in board[i:i+3]):
            return True
    
    # Check for winning columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
            
    # Check for winning diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
        
    return False

def minimax(board, is_maximizing):
    """
    Minimax algorithm with alpha-beta pruning to find the best move.
    'X' is the minimizing player (computer), 'O' is the maximizing player (human).
    The AI plays as 'X' and will always make the optimal move.
    """
    # Define the players and the opponent for clarity
    ai_player = 'X'
    human_player = 'O'
    
    # Check for a terminal state and return the score
    # Score for a win is +1, loss is -1, and tie is 0.
    if check_winner(board, ai_player):
        return 1, None
    if check_winner(board, human_player):
        return -1, None
    if not available_moves(board):
        return 0, None

    if is_maximizing:
        # The AI is the maximizing player
        best_score = -math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = ai_player
            score, _ = minimax(board, False)
            board[move] = ' '  # Undo the move

            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        # The human is the minimizing player
        best_score = math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = human_player
            score, _ = minimax(board, True)
            board[move] = ' '  # Undo the move

            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def get_computer_move(board):
    """Gets the optimal move for the computer using Minimax."""
    # The AI is the maximizing player, so we call minimax with True.
    _, best_move = minimax(board, True)
    return best_move

def get_player_move(board):
    """Gets a valid move from the human player."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if move not in available_moves(board):
                print("Invalid move. Please enter a number from 1-9 that is not taken.")
            else:
                return move
        except ValueError:
            print("Invalid input. Please enter a number.")

def play_game():
    """The main function to run the Tic-Tac-Toe game loop."""
    board = [' '] * 9
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    # Let the human player ('O') go first.
    turn = 'O'

    while True:
        if turn == 'O':
            # Human's turn
            move = get_player_move(board)
            board[move] = 'O'
        else:
            # Computer's turn
            print("Computer is thinking...")
            move = get_computer_move(board)
            board[move] = 'X'

        print(f"Player {turn} makes a move to square {move + 1}")
        print_board(board)

        # Check for a winner after the move
        if check_winner(board, turn):
            print(f"{turn} wins!")
            break

        # Check for a tie
        if not available_moves(board):
            print("It's a draw!")
            break

        # Switch turns
        turn = 'X' if turn == 'O' else 'O'

if __name__ == "__main__":
    play_game()
