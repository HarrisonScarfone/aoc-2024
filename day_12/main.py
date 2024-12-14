# FILEPATH = "day_12/test_input.txt"
FILEPATH = "day_12/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

# Part 1

# is_out_of_bounds = lambda arr,i,j : i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0])

# def check_connections(arr, i, j, plant):
#     valid_connections = []
#     if not is_out_of_bounds(arr, i+1, j) and arr[i+1][j] == plant:
#         valid_connections.append((i+1, j))
#     if not is_out_of_bounds(arr, i, j+1) and arr[i][j+1] == plant:
#         valid_connections.append((i, j+1))
#     if not is_out_of_bounds(arr, i-1, j) and arr[i-1][j] == plant:
#         valid_connections.append((i-1, j))
#     if not is_out_of_bounds(arr, i, j-1) and arr[i][j-1] == plant:
#         valid_connections.append((i, j-1))
#     return valid_connections

# def get_enclosed_region(arr, i, j, plant):
#     nodes_to_check = [(i, j)]
#     seen = set()
#     connections = 0
#     nodes = 0

#     while nodes_to_check:
#         node = nodes_to_check.pop()

#         if node in seen:
#             continue

#         seen.add(node)
#         nodes += 1
#         i, j = node
#         valid_connections = check_connections(arr, i, j, plant)

#         new_nodes = [val for val in valid_connections if val not in seen]
#         connections += len(new_nodes)
#         nodes_to_check += new_nodes

#     return nodes, (4 * nodes) - (2 * connections), seen

# def get_fence_cost(regions):
#     cost = 0
#     for region in regions:
#         _, area, perimeter = region
#         cost += (area * perimeter)
#     return cost

# def solve():
#     arr = []
#     for line in read_input(FILEPATH):
#         arr.append(list(line.strip()))

#     # regions like (plant, area, perim)
#     regions = []
#     seen = set()
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             # Its already a valid node in a valid region
#             if (i, j) in seen:
#                 continue
#             area, perimeter, newly_seen = get_enclosed_region(arr, i, j, arr[i][j])
#             seen.update(newly_seen)
#             regions.append((arr[i][j], area, perimeter))

#     print(regions)
#     cost = get_fence_cost(regions)
#     print(cost)     

# solve()

# Part 2

# Ok first of WTF. Now to business...

def get_directions_of_val(arr, i, j, val, look_for_val):
    directions = []
    for dir in [(1, (0, 1)), (2, (1, 0)), (3, (0, -1)), (4, (-1, 0))]:
        d, (n, m) = dir
        n += i
        m += j
        if look_for_val:
            if arr[n][m] == val:
                directions.append((d, (n, m)))
        else:
            if arr[n][m] != val:
                directions.append((d, (n, m)))
    return directions

def count_exterior_corners(arr, i, j):
    plant = arr[i][j]
    u = arr[i-1][j]
    ur = arr[i-1][j+1]
    r = arr[i][j+1]
    dr = arr[i+1][j+1]
    d = arr[i+1][j]
    dl = arr[i+1][j-1]
    l = arr[i][j-1]
    ul = arr[i-1][j-1]
    exterior_corners = 0
    if u == plant and r == plant and ur != plant:
        exterior_corners += 1
    if r == plant and d == plant and dr != plant:
        exterior_corners += 1
    if d == plant and l == plant and dl != plant:
        exterior_corners += 1
    if l == plant and u == plant and ul != plant:
        exterior_corners += 1
    return exterior_corners

def count_interior_corners(wall_dirs):
    if len(wall_dirs) in [0, 1]:
        return 0
    if len(wall_dirs) == 2:
        if wall_dirs[0] in [1, 3] and wall_dirs[1] in [2, 4]:
            return 1
        elif wall_dirs[0] in [2, 4] and wall_dirs[1] in [1, 3]:
            return 1
        else:
            return 0
    return (count_interior_corners([wall_dirs[0], wall_dirs[1]]) +
            count_interior_corners([wall_dirs[0], wall_dirs[2]]) +
            count_interior_corners([wall_dirs[1], wall_dirs[2]]))

def count_walls_of_area(arr, i, j, seen):
    nodes_to_check = [(i, j)]
    total_nodes = 1
    corners = 0
    plant = arr[i][j]
    seen.add((i, j))

    while nodes_to_check:
        node = nodes_to_check.pop()
        i, j = node
        curr_walls = get_directions_of_val(arr, i, j, plant, False)

        wall_dirs = [d for d, _ in curr_walls]
        new_corners = count_interior_corners(wall_dirs) + count_exterior_corners(arr, i, j)
        corners += new_corners

        connections = get_directions_of_val(arr, i, j, plant, True)
        for connection in connections:
            _, potential_node = connection
            if potential_node not in seen:
                total_nodes += 1
                seen.add(potential_node)
                nodes_to_check.insert(0, potential_node)

    if total_nodes == 1:
        corners = 4
    return total_nodes, corners

def solve():
    arr = []
    for line in read_input(FILEPATH):
        arr.append(["-"] + list(line.strip()) + ["-"])

    arr.insert(0, ["-" for _ in range(len(arr[0]))])
    arr.append(["-" for _ in range(len(arr[0]))])

    seen = set()
    total_cost = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (i, j) in seen or arr[i][j] == "-":
                continue
            area, sides = count_walls_of_area(arr, i, j, seen)
            total_cost += area * sides
    
    print(total_cost)     

solve()
