import random
import math
def calculate_attacks(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i+1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks

def generate_initial_state(n):
    return [random.randint(0, n-1) for _ in range(n)]

def display_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()

def get_neighbors(board):
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if row != board[col]:  # Skip if the queen is already in this row
                new_board = board[:]
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors

# Hill climbing algorithm for solving N-Queens problem
def hill_climbing(n):
    # Start with a random initial configuration
    current_state = generate_initial_state(n)
    current_cost = calculate_attacks(current_state)
    
    print("Initial board:")
    display_board(current_state)
    
    # Keep climbing until we reach a solution or no improvement can be made
    while current_cost > 0:
        neighbors = get_neighbors(current_state)
        best_neighbor = None
        best_cost = current_cost
        
        # Evaluate each neighbor and choose the one with the least attacks
        for neighbor in neighbors:
            neighbor_cost = calculate_attacks(neighbor)
            if neighbor_cost < best_cost:
                best_neighbor = neighbor
                best_cost = neighbor_cost
        
        # If no improvement, break (local maximum reached)
        if best_cost == current_cost:
            break
        
        # Move to the best neighbor
        current_state = best_neighbor
        current_cost = best_cost
        
        print(f"Move to new board with {current_cost} attacks:")
        display_board(current_state)
    if current_cost == 0:
            print("Solution found!")
    
    # Return the final configuration and the number of attacks (should be 0 for a solution)
    return current_state, current_cost

# Simulated Annealing algorithm for solving N-Queens problem
# Change cooling rate and max iterations:
def simulated_annealing(n, initial_temperature=1000, cooling_rate=0.95, max_iterations=50):
    # Start with a random initial configuration
    current_state = generate_initial_state(n)
    current_cost = calculate_attacks(current_state)
    temperature = initial_temperature

    print("Initial board (Simulated Annealing):")
    display_board(current_state)

    for iteration in range(max_iterations):
        if current_cost == 0:
            print("Solution found!")
            break

        neighbors = get_neighbors(current_state)
        best_neighbor = random.choice(neighbors)
        best_cost = calculate_attacks(best_neighbor)

        delta_cost = best_cost - current_cost

        # Avoid division by zero error by using max with a small value
        if delta_cost < 0 or random.random() < math.exp(-delta_cost / max(temperature, 1e-10)):
            current_state = best_neighbor
            current_cost = best_cost

            print(f"Move to new board with {current_cost} attacks (iteration {iteration + 1}):")
            display_board(current_state)

        temperature *= cooling_rate

    if current_cost != 0:
        print(f"Finished without finding perfect solution. Final attacks: {current_cost}")
    
    return current_state, current_cost


# Example usage:
n = 4  # Size of the board (4 queens)
print("\nRunning Hill Climbing...")
hill_solution, hill_attacks = hill_climbing(n)

print("\nRunning Simulated Annealing...")
sa_solution, sa_attacks = simulated_annealing(n)
