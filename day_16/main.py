# FILEPATH = "day_16/test_input.txt"
FILEPATH = "day_16/input.txt"

def read_input(filepath): 
    with open(filepath, "r") as f:
        return f.readlines()
    
# # Part 1

# def cost_to_rotate(curr, target):
#     if curr == target:
#         return 0
#     if abs(curr - target) == 2:
#         return 2000
#     return 1000

# def get_next_positions(maze, curr, curr_direction):
#     i, j = curr
#     next_squares = []
#     if maze[i-1][j] in [".", "E"]:
#         next_squares.append((1, 1+cost_to_rotate(curr_direction, 1), i-1, j))
#     if maze[i][j+1] in [".", "E"]:
#         next_squares.append((2, 1+cost_to_rotate(curr_direction, 2), i, j+1))
#     if maze[i+1][j] in [".", "E"]:
#         next_squares.append((3, 1+cost_to_rotate(curr_direction, 3), i+1, j))
#     if maze[i][j-1] in [".", "E"]:
#         next_squares.append((4, 1+cost_to_rotate(curr_direction, 4), i, j-1))
#     return next_squares

# import heapq

# def backtrace_path(node, ancestors):
#     paths = []
#     if not ancestors.get(node, None):
#         return [[node]]
#     for ancestor in ancestors[node]:
#         for path in backtrace_path(ancestor, ancestors):
#             paths.append(path + [node])
#     return paths

# def shortest_path(maze):
#     distances = {}
#     ancestors = {}
#     start = None
#     terminal_node = None
#     for i in range(len(maze)):
#         for j in range(len(maze[0])):
#             if maze[i][j] == ".":
#                 distances[(i, j)] = float("inf")
#                 ancestors[(i, j)] = []
#             elif maze[i][j] == "S":
#                 start = (i, j)
#                 distances[start] = 0
#             elif maze[i][j] == "E":
#                 terminal_node = (i, j)
#                 ancestors[(i, j)] = []
#                 distances[(i, j)] = float("inf")

#     to_check = [(0, 2, start)]
#     while to_check:
#         curr_distance, curr_direction, curr_node = heapq.heappop(to_check)
#         if curr_distance > distances[curr_node]:
#             continue
#         for new_direction, extra_distance, next_i, next_j in get_next_positions(maze, curr_node, curr_direction):
#             new_distance = curr_distance + extra_distance

#             if new_distance < distances[(next_i, next_j)]:
#                 distances[(next_i, next_j)] = new_distance
#                 ancestors[(next_i, next_j)] = [curr_node]
#                 heapq.heappush(to_check, (new_distance, new_direction, (next_i, next_j)))
#             elif new_distance == distances[(next_i, next_j)]:
#                 ancestors[(next_i, next_j)] = ancestors[(next_i, next_j)] + [curr_node]
    
#     best_distance = distances[terminal_node]
#     best_path = backtrace_path(terminal_node, ancestors)

#     return best_distance

# def solve():
#     maze = []
#     for line in read_input(FILEPATH):
#         maze.append(list(line.strip()))

#     print(shortest_path(maze))

# solve()

# Part 2

def backtrace_path(node, ancestors):
    paths = []
    if not ancestors.get(node, None):
        return [[node]]
    for ancestor in ancestors[node]:
        for path in backtrace_path(ancestor, ancestors):
            paths.append(path + [node])
    return paths

def cost_to_rotate(curr, target):
    if curr == target:
        return 0
    if abs(curr - target) == 2:
        return 2000
    return 1000

def get_next_positions(maze, curr):
    curr_direction, i, j = curr
    next_squares = []
    if maze[i-1][j] in [".", "E"]:
        next_squares.append((1, i-1, j))
    if maze[i][j+1] in [".", "E"]:
        next_squares.append((2, i, j+1))
    if maze[i+1][j] in [".", "E"]:
        next_squares.append((3, i+1, j))
    if maze[i][j-1] in [".", "E"]:
        next_squares.append((4, i, j-1))
    real_next_squares = []
    for square in next_squares:
        d, n, m = square
        if d != curr_direction:
            real_next_squares.append((1000, (d, i, j)))
        else:
            real_next_squares.append((1, (d, n, m)))       
    
    return real_next_squares

import heapq

def shortest_path(maze):
    distances = {}
    ancestors = {}
    start = None
    terminal_node = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == ".":
                for k in range(1, 5):
                    distances[(k, i, j)] = float("inf")
                    ancestors[(k, i, j)] = []
            elif maze[i][j] == "S":
                for k in range(1, 5):
                    start = (k, i, j)
                    distances[start] = float("inf")
                    ancestors[(k, i, j)] = []
                start = (2, i, j)
                distances[start] = 0
            elif maze[i][j] == "E":
                terminal_node = (i, j)
                for k in range(1, 5):
                    ancestors[(k, i, j)] = []
                    distances[(k, i, j)] = float("inf")

    to_check = [(0, start)]
    while to_check:
        curr_distance, curr_node = heapq.heappop(to_check)
        if curr_distance > distances[curr_node]:
            continue
        for new_distance, (new_direction, next_i, next_j) in get_next_positions(maze, curr_node):
            new_distance = curr_distance + new_distance

            if new_distance < distances[(new_direction, next_i, next_j)]:
                distances[(new_direction, next_i, next_j)] = new_distance
                ancestors[(new_direction, next_i, next_j)] = [curr_node]
                heapq.heappush(to_check, (new_distance, (new_direction, next_i, next_j)))
                a = 0
            elif new_distance == distances[(new_direction, next_i, next_j)]:
                ancestors[(new_direction, next_i, next_j)] = ancestors[(new_direction, next_i, next_j)] + [curr_node]
    
    min_cost = float('inf')
    min_node = None
    for i in range(1, 5):
        if distances[i, terminal_node[0], terminal_node[1]] < min_cost:
            min_cost = distances[i, terminal_node[0], terminal_node[1]]
            min_node = (i, terminal_node[0], terminal_node[1])

    min_paths = backtrace_path(min_node, ancestors)
    unique_minpath_nodes = set()
    for path in min_paths:
        for node in path:
            unique_minpath_nodes.add((node[1], node[2]))
    
    return f"min cost: {min_cost}\nmin path node count: {len(unique_minpath_nodes)}"

def solve():
    maze = []
    for line in read_input(FILEPATH):
        maze.append(list(line.strip()))

    print(shortest_path(maze))

solve()
