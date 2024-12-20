# FILEPATH = "day_18/test_input.txt"
FILEPATH = "day_18/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()
    

# Part 1

import heapq


# GRID_HEIGHT = 7
# GRID_WIDTH = 7
# SIM = 12

GRID_HEIGHT = 71
GRID_WIDTH = 71
SIM = 1024

def update_grid(grid, xys, num_bytes):
    for i in range(num_bytes):
        n, m = xys[i]
        grid[m][n] = '#'

def get_neighbours(grid, i, j):
    neighbours = []
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        n, m = i + di, j + dj
        if grid[n][m] == ".":
            neighbours.append((n, m))
    return neighbours

def solve_grid(grid):
    distances = {}
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == ".":
                distances[(i, j)] = float("inf")

    start = (1, 1)
    distances[(start)] = 0
    to_visit = [(0, start)]
    seen = set()

    while to_visit:
        curr_distance, curr_node = heapq.heappop(to_visit)
        i, j = curr_node
        if curr_node in seen:
            continue
        seen.add(curr_node)

        for neighbour in get_neighbours(grid, i, j):
            if neighbour in seen:
                continue
            new_distance = curr_distance + 1

            if new_distance < distances[neighbour]:
                distances[neighbour] = new_distance
                heapq.heappush(to_visit, (new_distance, neighbour))

    return distances[(GRID_HEIGHT, GRID_WIDTH)]


def solve():
    grid = [["#" for _ in range(GRID_WIDTH+2)]]
    for _ in range(GRID_HEIGHT):
        grid.append(["#"] + ["." for _ in range(GRID_WIDTH)] + ["#"])
    grid.append(["#" for _ in range(GRID_WIDTH+2)])

    xys = []
    for line in read_input(FILEPATH):
        xys.append([int(x)+1 for x in line.strip().split(",")])

    xys = [(x[0], x[1]) for x in xys]

    # just don't use this part for p1
    for k in range(1024, 3450):
        update_grid(grid, xys, k)
        r = solve_grid(grid)
        if r == float("inf"):
            print(k)
            break

    print(r)
solve()