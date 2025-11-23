# Initialize room (2x2 grid), each cell could be 'dirty' or 'clean'
room = [
    ['dirty', 'clean'],
    ['dirty', 'dirty']
]
# Starting position
x, y = 0, 0

# Function to check if the current cell is dirty
def is_dirty(x, y):
    return room[x][y] == 'dirty'

# Function to clean the current cell
def clean(x, y):
    room[x][y] = 'clean'
    print(f"Cleaned cell ({x},{y})")

# Function to move to a new position (up, down, left, or right)
def move_to(new_x, new_y):
    global x, y
    x, y = new_x, new_y
    print(f"Moved to ({x},{y})")

# Function to check if all cells are clean
def all_clean():
    for i in range(2):
        for j in range(2):
            if room[i][j] == 'dirty':
                return False
    return True

# Cleaning path: Visit each cell and clean (left to right, top to bottom)
# The allowed moves are up, down, left, right
cleaning_path = [(0, 0), (0, 1), (1, 1), (1, 0)]

# Start cleaning the room following the path
for cell in cleaning_path:
    move_to(cell[0], cell[1])
    if is_dirty(cell[0], cell[1]):
        clean(cell[0], cell[1])

# Final check to see if the room is clean
if all_clean():
    print("Room is clean!")
else:
    print("Some cells are still dirty.")
