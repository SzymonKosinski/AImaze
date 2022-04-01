

# Function to find a route using the Depth-first Search algorithm.

# Depth-first search is an algorithm used to traverse a tree or generate nodes and paths in a tree. This algorithm
# starts at a specific node and explores paths of connected nodes of the first child and does this recursively until
# it reaches the furthest leaf node before backtracking and exploring other paths to leaf nodes via other child nodes
# that have been visited.

# Although the Depth-first search algorithm van be implemented with a recursive function. This implementation is
# achieved using a stack to better represent the order of operations as to which nodes get visited and processed.
# It is important to keep track of the visited points so that the same nodes do not get visited unnecessarily and
# create cyclic loops.
def run_dfs(maze_puzzle, current_point, visited_points):
    # TODO: Dla podstawowej postaci labiryntu wynik powinien być identyczny jak w BFS.
    stack = []
    stack.append(current_point)
    visited_points.append(current_point)
    print("testing...")
    while stack:
        # Set the next node in the queue as the current node
        current_point = stack.pop()
        # Get the neighbors of the current node
        neighbors = maze_puzzle.get_neighbors(current_point)

        # Iterate through the neighbors of the current node
        for neighbor in neighbors:
            # Add the neighbor to the queue if it hasn't been visited
            if not is_in_visited_points(neighbor, visited_points):
                neighbor.set_parent(current_point)
                stack.append(neighbor)
                visited_points.append(neighbor)

                # Return the path to the current neighbor if it is the goal
                if maze_puzzle.get_current_point_value(neighbor) == '*':
                    return neighbor
    # In the case that no path to the goal was found
    return 'No path to the goal found.'


# Function to determine if the point has already been visited
def is_in_visited_points(current_point, visited_points):
    for visited_point in visited_points:
        if current_point.x == visited_point.x and current_point.y == visited_point.y:
            return True
    return False

def show_elements(stack):
    for i in range(len(stack)):
        print(str(stack[i].x) + " " + str(stack[i].y))

'''start = time.time()
print('---Depth-first Search---')

# Initialize a MazePuzzle
maze_game_main = mp.MazePuzzle(5,5)

# Run the depth first search algorithm with the initialized maze
starting_point = mp.Point(int(maze_game_main.maze_size_x/2), int(maze_game_main.maze_size_y/2))
outcome = run_dfs(maze_game_main, starting_point, [])

# Get the path found by the depth first search algorithm
dfs_path = mp.get_path(outcome)

# Print the results of the path found
print('Path Length: ', len(dfs_path))
maze_game_main.overlay_points_on_map(dfs_path)
print('Path Cost: ', mp.get_path_cost(outcome))
for point in dfs_path:
    print('Point: ', point.x, ',', point.y)
end = time.time()
print("czas wykonania programu wynosi: ")
print(end-start)
'''