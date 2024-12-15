# FILEPATH = "day_15/test_input.txt"
FILEPATH = "day_15/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

def show_grid(warehouse):
    for row in warehouse:
        print(row)

# # Part 1

# def get_new_coordinates_from_direction(start, movement):
#     i, j = start
#     if movement == "^":
#         return (i-1, j)
#     elif movement == ">":
#         return (i, j+1)
#     elif movement == "v":
#         return (i+1, j)
#     elif movement == "<":
#         return (i, j-1)

# def move_boxes(warehouse, i, j, movement):
#     i2, j2 = get_new_coordinates_from_direction((i, j), movement)
#     i_robot, j_robot = i2, j2
#     moves = []
#     while warehouse[i2][j2] == "O":
#         next_move = get_new_coordinates_from_direction((i2, j2), movement)
#         moves.append(next_move)
#         i2, j2 = next_move

#     if warehouse[i2][j2] == "#":
#         return None, None
    
#     for move in moves:
#         n, m = move
#         warehouse[n][m] = "O"

#     warehouse[i_robot][j_robot] = "@"
#     warehouse[i][j] = "."
#     return (i_robot, j_robot)

# def calculate_score(warehouse):
#     score = 0
#     for i in range(len(warehouse)):
#         for j in range(len(warehouse[0])):
#             if warehouse[i][j] == "O":
#                 score += 100 * i + j
#     return score

# def simulate_robot(warehouse, robot, movements):
#     for movement in movements:
#         i, j = robot
#         i2, j2 = get_new_coordinates_from_direction(robot, movement)
#         if warehouse[i2][j2] == "#":
#             continue
#         if warehouse[i2][j2] == ".":
#             warehouse[i][j] = "."
#             warehouse[i2][j2] = "@"
#             robot = (i2, j2)
#             continue
#         # else its boxes time
#         new_i, new_j = move_boxes(warehouse, i, j, movement)
#         if new_i:
#             robot = (new_i, new_j)

# def solve():
#     warehouse = []
#     robot = None
#     movements = []
#     for i, line in enumerate(read_input(FILEPATH)):
#         txt = line.strip()
#         if not txt:
#             continue
#         if txt.startswith("#"):
#             if txt.find("@") > -1:
#                 robot = (i, txt.find("@"))
#             warehouse.append(list(txt))
#             continue
        
#         movements += (list(txt))

#     simulate_robot(warehouse, robot, movements)
#     print(calculate_score(warehouse))

# solve()
        
# Part 2

# Get so freakin tired of these....
# Do this one with regex so I can flex my web dev regex ability to Paul during morning coffee.

import re

class DirectionMatchers:
    def __init__(self):
        self.right_match = self._make_right_match()
        self.left_match = self._make_left_match()
    
    def _make_right_match(self):
        rstr = r"@([\[\]]+)\."
        return re.compile(rstr)
    
    def _make_left_match(self):
        lstr = r"\.([\[\]]+)@"
        return re.compile(lstr)

def get_new_coordinates_from_direction(start, movement):
    i, j = start
    if movement == "^":
        return (i-1, j)
    elif movement == ">":
        return (i, j+1)
    elif movement == "v":
        return (i+1, j)
    elif movement == "<":
        return (i, j-1)
    
def vertical_search(warehouse, p, q, is_up):
    curr_layer = [(p, q)]
    next_layer = []
    remove_pairs = []
    add_pairs = []
    dy = -1 if is_up else 1
    while curr_layer:
        node = curr_layer.pop()
        i, j = node
        if warehouse[i][j] == "]":
            remove_pairs.append(((i, j-1), (i, j)))
            add_pairs.append(((i+dy,j-1), (i+dy,j)))
            next_layer.insert(0, (i+dy, j))
            next_layer.insert(0, (i+dy, j-1))
        elif warehouse[i][j] == "[":
            remove_pairs.append(((i, j), (i, j+1)))
            add_pairs.append(((i+dy,j), (i+dy,j+1)))
            next_layer.insert(0, (i+dy, j))
            next_layer.insert(0, (i+dy, j+1))
        elif warehouse[i][j] == "#":
            return (p-dy, q)
        
        if not curr_layer:
            curr_layer = next_layer
            next_layer = []
    
    for add, remove in zip(reversed(add_pairs), reversed(remove_pairs)):
        (ali, alj), (_, arj) = add
        (rli, rlj), (_, rrj) = remove
        warehouse[rli] = warehouse[rli][:rlj] + ".." + warehouse[rli][rrj+1:]
        warehouse[ali] = warehouse[ali][:alj] + "[]" + warehouse[ali][arj+1:]
    
    warehouse[p] = warehouse[p][:q] + "@" + warehouse[p][q+1:]
    warehouse[p-dy] = warehouse[p-dy][:q] + "." + warehouse[p-dy][q+1:]
    return (p, q)


def move_boxes(warehouse, i, j, movement, d):
    if movement == ">":
        row = warehouse[i]
        rmatch = d.right_match.search(row)
        if rmatch:
            group = rmatch.group(1)
            sidx = int(rmatch.start()) + 1
            boxes = len(group) // 2
            tmp = row[:sidx-1] + "." + "@" + "[]" * boxes + row[sidx+(2*boxes)+1:]
            warehouse[i] = tmp
            return (i, tmp.index("@"))
        return(i, j-1)
    elif movement == "<":
        row = warehouse[i]
        lmatch = d.left_match.search(row)
        if lmatch:
            group = lmatch.group(1)
            sidx = int(lmatch.start()) + 1
            boxes = len(group) // 2
            tmp = row[:sidx-1] + "[]" * boxes + "@" + "." + row[sidx+(2*boxes)+1:]
            warehouse[i] = tmp
            return (i, tmp.index("@"))
        return (i, j+1)
    elif movement == "^":
        return vertical_search(warehouse, i, j, True)
    elif movement == "v":
        return vertical_search(warehouse, i, j, False)
    else:
        assert(False)

def calculate_score(warehouse):
    score = 0
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "[":
                score += 100 * i + j
    return score

def simulate_robot(warehouse, robot, movements):
    d = DirectionMatchers()
    for movement in movements:
        i, j = robot
        i2, j2 = get_new_coordinates_from_direction(robot, movement)
        if warehouse[i2][j2] == "#":
            continue
        if warehouse[i2][j2] == ".":
            warehouse[i] = warehouse[i][:j] + "." + warehouse[i][j+1:]
            warehouse[i2] = warehouse[i2][:j2] + "@" + warehouse[i2][j2+1:]
            robot = (i2, j2)
            continue
        robot = move_boxes(warehouse, i2, j2, movement, d)

def solve():
    warehouse = []
    robot = None
    movements = []
    for i, line in enumerate(read_input(FILEPATH)):
        txt = line.strip()
        if not txt:
            continue
        if txt.startswith("#"):
            raw_input = list(txt)
            expanded_line = []
            for char in raw_input:
                if char == "#":
                    expanded_line.append("##")
                elif char == "O":
                    expanded_line.append("[]")
                elif char == ".":
                    expanded_line.append("..")
                elif char == "@":
                    expanded_line.append("@.")
            expanded_line = "".join(expanded_line)
            expanded_line = list(expanded_line)
            if "@" in expanded_line:
                robot = (i, expanded_line.index("@"))
            warehouse.append("".join(expanded_line))
        else:
            movements += list(txt)

    simulate_robot(warehouse, robot, movements)
    print(calculate_score(warehouse))

solve()
        