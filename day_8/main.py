# FILEPATH = "day_8/test_input.txt"
FILEPATH = "day_8/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()



# Part 1

# import itertools

# def get_node_locations(arr):
#     nodes = {}
#     for i in range(len(arr)):
#         for j in range(len(arr[0])):
#             if arr[i][j] != ".":
#                 nodes[arr[i][j]] = nodes.get(arr[i][j], []) + [(i, j)]
#     return nodes

# in_bounds = lambda arr, i, j : i > -1 and j > -1 and i < len(arr) and j < len(arr[0])


# def get_antinode_locations(arr, nodes):
#     if len(nodes) == 1:
#         return []
    
#     node_pairs = itertools.combinations(nodes, 2)

#     antinode_locations = set()
#     for pair in node_pairs:
#         c1, c2 = pair
#         dx = c2[0] - c1[0]
#         dy = c2[1] - c1[1]
#         a1 = (c1[0] + (-1 * dx), c1[1] + (-1 * dy))
#         a2 = (c2[0] + dx, c2[1] + dy)
        
#         if in_bounds(arr, a1[0], a1[1]):
#             antinode_locations.add(a1)
#         if in_bounds(arr, a2[0], a2[1]):
#             antinode_locations.add(a2)

#     return antinode_locations


# def solve():
#     arr = []
#     for line in read_input(FILEPATH):
#         arr.append([val for val in list(line.strip())])

#     nodes = get_node_locations(arr)
#     antinodes = set()
#     for key in nodes:
#         antinodes.update(get_antinode_locations(arr, nodes[key]))

#     for antinode in antinodes:
#         i, j = antinode
#         arr[i][j] += "#"

#     for row in arr:
#         print("".join(row))

#     print(len(antinodes))
# solve()

# Part 2

import itertools

def get_node_locations(arr):
    nodes = {}
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != ".":
                nodes[arr[i][j]] = nodes.get(arr[i][j], []) + [(i, j)]
    return nodes

in_bounds = lambda arr, i, j : i > -1 and j > -1 and i < len(arr) and j < len(arr[0])
coor_from_reflected_slope = lambda i, j, dx, dy : (i + (-1 * dx), j + (-1 * dy))
coor_from_slope = lambda i, j, dx, dy : (i + dx, j + dy)

def get_antinode_locations(arr, nodes):
    if len(nodes) == 1:
        return []
    
    node_pairs = itertools.combinations(nodes, 2)

    antinode_locations = set()
    for pair in node_pairs:
        c1, c2 = pair
        dx = c2[0] - c1[0]
        dy = c2[1] - c1[1]

        i, j = coor_from_reflected_slope(c1[0], c1[1], dx, dy)
        while in_bounds(arr, i, j):
            antinode_locations.add((i, j))
            i, j = coor_from_reflected_slope(i, j, dx, dy)

        i, j = coor_from_slope(c2[0], c2[1], dx, dy)
        while in_bounds(arr, i, j):
            antinode_locations.add((i, j))
            i, j = coor_from_slope(i, j, dx, dy)
        
        antinode_locations.add(c1)
        antinode_locations.add(c2)

    return antinode_locations


def solve():
    arr = []
    for line in read_input(FILEPATH):
        arr.append([val for val in list(line.strip())])

    nodes = get_node_locations(arr)
    antinodes = set()
    for key in nodes:
        antinodes.update(get_antinode_locations(arr, nodes[key]))

    for antinode in antinodes:
        i, j = antinode
        arr[i][j] += "#"

    for row in arr:
        print("".join(row))

    print(len(antinodes))

solve()