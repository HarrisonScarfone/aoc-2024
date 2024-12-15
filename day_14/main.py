# FILEPATH = "day_14/test_input.txt"
FILEPATH = "day_14/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

# Part 1

# WIDTH = 101
# HEIGHT = 103
# ITERS = 100

# def get_new_position(px, py, vx, vy, width=WIDTH, height=HEIGHT):
#     new_x = px + vx
#     if new_x >= WIDTH:
#         new_x -= WIDTH
#     elif new_x < 0:
#         new_x += WIDTH

#     new_y = py + vy
#     if new_y >= HEIGHT:
#         new_y -= HEIGHT
#     elif new_y < 0:
#         new_y += HEIGHT
#     return (new_x, new_y)

# def solve():
#     curr_robots = {}
#     for rid, line in enumerate(read_input(FILEPATH)):
#         p, v = line.strip().split()
#         p = p.replace("p=", "")
#         v = v.replace("v=", "")
#         px, py = p.split(",")
#         vx, vy = v.split(",")
#         curr_robots[(int(px), int(py), rid)] = (int(vx), int(vy))

#     next_robots = {}
#     for _ in range(ITERS):
#         for robot in curr_robots.keys():
#             px, py, rid = robot
#             vx, vy = curr_robots[robot]
#             nx, ny = get_new_position(px, py, vx, vy)
#             new_position = (nx, ny, rid)
#             next_robots[new_position] = curr_robots[robot]
#         curr_robots = next_robots.copy()
#         next_robots.clear()

#     # width 11 height 7 -> 5, 3 -> i < 6, j < 4
#     # 0,1,2,3,4,5 6 7,8,9,10,11
#     is_quad_1 = lambda i,j : i < (WIDTH // 2) and j < (HEIGHT // 2) 
#     is_quad_2 = lambda i,j : i < (WIDTH // 2) and j > (HEIGHT // 2) 
#     is_quad_3 = lambda i,j : i > (WIDTH // 2) and j < (HEIGHT // 2) 
#     is_quad_4 = lambda i,j : i > (WIDTH // 2) and j > (HEIGHT // 2) 

#     q1, q2, q3, q4 = 0, 0, 0, 0
#     for robot in curr_robots:
#         i, j, rid = robot
#         if is_quad_1(i, j):
#             q1 += 1
#         elif is_quad_2(i, j):
#             q2 += 1
#         elif is_quad_3(i, j):
#             q3 += 1
#         elif is_quad_4(i, j):
#             q4 += 1         

# solve()


# Part 2

import numpy as np
from scipy.signal import convolve2d

WIDTH = 101
HEIGHT = 103
ITERS = 25000

def dump_pattern_to_file(nodes, iter):
    grid = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]

    for node in nodes:
        x, y, _ = node
        grid[x][y] = 1

    kernel = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    
    A = np.array(grid)
    k = np.array(kernel)
    result = convolve2d(A, kernel, mode='same', boundary='fill', fillvalue=0)
    target = sum(np.ndarray.flatten(k))
    if np.any(result == target):
        print(iter)
    # If you wanna see the m*****f****ing tree... mine was sidesways lel.
    #     with open("treefile.txt", "a") as f:
    #         f.write("\n\n")
    #         f.write(f"===================\niter: {iter}\n===============================\n\n")
    #         for line in grid:
    #             f.write("".join([" " if x == 0 else "@" for x in line]) + "\n")
    #         f.write("\n\n")

def get_new_position(px, py, vx, vy, width=WIDTH, height=HEIGHT):
    new_x = px + vx
    if new_x >= WIDTH:
        new_x -= WIDTH
    elif new_x < 0:
        new_x += WIDTH

    new_y = py + vy
    if new_y >= HEIGHT:
        new_y -= HEIGHT
    elif new_y < 0:
        new_y += HEIGHT
    return (new_x, new_y)

is_quad_1 = lambda i,j : i < (WIDTH // 2) and j < (HEIGHT // 2) 
is_quad_2 = lambda i,j : i < (WIDTH // 2) and j > (HEIGHT // 2) 
is_quad_3 = lambda i,j : i > (WIDTH // 2) and j < (HEIGHT // 2) 
is_quad_4 = lambda i,j : i > (WIDTH // 2) and j > (HEIGHT // 2) 

def get_safety_score(robots):
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in robots:
        i, j, rid = robot
        if is_quad_1(i, j):
            q1 += 1
        elif is_quad_2(i, j):
            q2 += 1
        elif is_quad_3(i, j):
            q3 += 1
        elif is_quad_4(i, j):
            q4 += 1
    return q1 * q2 * q3 * q4

def solve():
    curr_robots = {}
    for rid, line in enumerate(read_input(FILEPATH)):
        p, v = line.strip().split()
        p = p.replace("p=", "")
        v = v.replace("v=", "")
        px, py = p.split(",")
        vx, vy = v.split(",")
        curr_robots[(int(px), int(py), rid)] = (int(vx), int(vy))

    next_robots = {}
    for i in range(ITERS):
        if len(curr_robots) == 500:
            dump_pattern_to_file(curr_robots, i)
        for robot in curr_robots.keys():
            px, py, rid = robot
            vx, vy = curr_robots[robot]
            nx, ny = get_new_position(px, py, vx, vy)
            new_position = (nx, ny, rid)
            next_robots[new_position] = curr_robots[robot]
        curr_robots = next_robots.copy()
        next_robots.clear()
    

solve()
