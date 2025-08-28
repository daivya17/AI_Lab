from collections import deque
import copy

# Define the goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Directions for moving the blank tile
DIRECTIONS = {
    'Up': (-1, 0),
    'Down': (1, 0),
    'Left': (0, -1),
    'Right': (0, 1)
}

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    for move, (dx, dy) in DIRECTIONS.items():
        new_x, new_y = x + dx, y + dy
        if is_valid(new_x, new_y):
            new_state = copy.deepcopy(state)
            # Swap blank with adjacent tile
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append((move, new_state))
    return neighbors

def bfs(start_state):
    queue = deque([(start_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        state_tuple = tuple(tuple(row) for row in current_state)

        if current_state == GOAL_STATE:
            return path  # Return the solution if we reach the goal state

        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        for move, neighbor in get_neighbors(current_state):
            queue.append((neighbor, path + [move]))

# Example usage
start_state = [[1, 2, 3],
                [8, 5, 6],
                [7, 0, 4]]

solution = bfs(start_state)

# Since we removed "no solution" handling, it will keep exploring until it finds the solution
if solution:
    print("Solution found in", len(solution), "moves:")
    print(" -> ".join(solution))
