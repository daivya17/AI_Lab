import math
import random
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
    Minimax algorithm to find the best move.
    'X' is the maximizing player (computer), 'O' is the minimizing player (human).
    """
    ai_player = 'X'
    human_player = 'O'
    
    if check_winner(board, ai_player):
        return 1, None
    if check_winner(board, human_player):
        return -1, None
    if not available_moves(board):
        return 0, None

    if is_maximizing:
        best_score = -math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = ai_player
            score, _ = minimax(board, False)
            board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move
    else:
        best_score = math.inf
        best_move = None
        for move in available_moves(board):
            board[move] = human_player
            score, _ = minimax(board, True)
            board[move] = ' '
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move

def get_computer_move(board):
    """
    Gets a beatable move for the computer. It finds all moves with a positive
    score and chooses one randomly. If no such moves exist, it chooses a
    random move to prolong the game.
    """
    ai_player = 'X'
    human_player = 'O'
    
    # If the board is empty, take the center.
    if not available_moves(board):
        return 4
    
    # Check for an immediate win for the computer
    for move in available_moves(board):
        board[move] = ai_player
        if check_winner(board, ai_player):
            board[move] = ' '
            return move
        board[move] = ' '

    # Check for an immediate block of the human player
    for move in available_moves(board):
        board[move] = human_player
        if check_winner(board, human_player):
            board[move] = ' '
            return move
        board[move] = ' '
    
    # If no immediate win or block, use a simplified minimax approach.
    # Find all moves that result in a positive score.
    positive_moves = []
    for move in available_moves(board):
        board[move] = ai_player
        score, _ = minimax(board, False)
        board[move] = ' '
        if score > 0:
            positive_moves.append(move)
            
    # If there are any moves that lead to a win or a draw, pick one at random.
    if positive_moves:
        return random.choice(positive_moves)
    
    # If all remaining moves lead to a loss, choose a random available move to delay the loss.
    return random.choice(available_moves(board))


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
