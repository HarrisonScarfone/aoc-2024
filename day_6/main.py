# FILEPATH = "day_6/test_input.txt"
FILEPATH = "day_6/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

# Part 1

# def rotate(direction):
#     if direction == "^":
#         return ">"
#     elif direction == ">":
#         return "v"
#     elif direction == "v":
#         return "<"
#     elif direction == "<":
#         return "^"
#     return -1

# def traverse(arr, i, j, direction):
#     count = 0
#     n, m  = None, None
#     while True:
#         if direction == "^":
#             n, m  = (i-1, j)
#         elif direction == ">":
#             n, m  = (i, j+1)
#         elif direction == "v":
#             n, m  = (i+1, j)
#         elif direction == "<":
#             n, m  = (i, j-1)
        
#         if n < 0 or m < 0 or n >= len(arr) or m >= len(arr[0]):
#             if arr[i][j] != "X":
#                 count += 1
#             return count
#         elif arr[n][m] == "#":
#             direction = rotate(direction)
#         else:
#             if arr[i][j] != "X":
#                 arr[i][j] = "X"
#                 count += 1
#             i, j = n, m

# def solve():
#     arr = []
#     for line in read_input(FILEPATH):
#         arr.append([elem for elem in line.strip()])

#     chars = ["^", ">", "<", "v"]
#     istart, jstart, direction = 0, 0, None
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] in chars:
#                 istart, jstart, direction = i, j, arr[i][j]

#     count = traverse(arr, istart, jstart, direction)

#     for l in arr:
#         print("".join(l))
#     print(count)

# solve()

# Part 2

import copy

def rotate(direction):
    if direction == "^":
        return ">"
    elif direction == ">":
        return "v"
    elif direction == "v":
        return "<"
    elif direction == "<":
        return "^"

def get_next_coordinates(i, j, direction):
    n, m = 0, 0
    if direction == "^":
        n, m  = (i-1, j)
    elif direction == ">":
        n, m  = (i, j+1)
    elif direction == "v":
        n, m  = (i+1, j)
    elif direction == "<":
        n, m  = (i, j-1)
    return n, m

def can_form_loop(arr, i, j, direction):
    seen = set()
    n, m  = None, None
    while True:
        if (i, j, direction) in seen:
            return 1
        else:
            seen.add((i, j, direction))

        n,m = get_next_coordinates(i, j, direction)
        if n < 0 or m < 0 or n >= len(arr) or m >= len(arr[0]):
            return 0

        if arr[n][m] == "#":
            direction = rotate(direction)
            continue

        i, j = n, m


def traverse(arr, i, j, direction):
    count = 0
    n, m  = None, None
    unique = 0
    start = (i, j, direction)
    while True:
        unique += 1 if arr[i][j] == "." or arr[i][j] == ".O" else 0
        arr[i][j] += direction if direction not in arr[i][j] else ""
        n,m = get_next_coordinates(i, j, direction)

        if n < 0 or m < 0 or n >= len(arr) or m >= len(arr[0]):
            print("unique: ", unique + 1)
            return count

        if arr[n][m] == "#":
            direction = rotate(direction)
            continue       
        else:
            if (n, m) != start:
                cpy = copy.deepcopy(arr)
                cpy[n][m] = "#"
                result = can_form_loop(cpy, start[0], start[1], start[2])
                if result > 0 and "O" not in arr[n][m]:
                    arr[n][m] += "O"
                    count += result

        i, j = n, m

def solve():
    arr = []
    for line in read_input(FILEPATH):
        arr.append([elem for elem in line.strip()])

    chars = ["^", ">", "<", "v"]
    istart, jstart, direction = 0, 0, None
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] in chars:
                istart, jstart, direction = i, j, arr[i][j]

    count = traverse(arr, istart, jstart, direction)

    print(count)


solve()
