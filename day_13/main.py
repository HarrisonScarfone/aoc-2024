# FILEPATH = "day_13/test_input.txt"
FILEPATH = "day_13/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()
    
# Part 1

import re
import numpy as np

IS_PART_2 = True

def tokens_required(adx, ady, bdx, bdy, tx, ty):
    # matrix solving ax = b
    a = np.array([[adx, bdx], [ady, bdy]])
    b = np.array([[tx], [ty]])
    x = np.linalg.solve(a, b).round().astype(int)
    f = np.ndarray.flatten(x)

    f0, f1 = f    
    if (f0 * adx + f1 * bdx) == tx and (f0 * ady + f1 * bdy) == ty:
        return int(f0) * 3 + int(f1)
    return 0

def solve():
    rstr = r"Button A: X\+(\d+), Y\+(\d+)\sButton B: X\+(\d+), Y\+(\d+)\sPrize: X=(\d+), Y=(\d+)"
    matcher = re.compile(rstr)

    token_count = 0
    with open(FILEPATH) as f:
        txt = f.read()
        for match in matcher.findall(txt):
            adx, ady, bdx, bdy, tx, ty = [int(elem) for elem in match]
            if IS_PART_2:
                tx, ty = tx + 10000000000000, ty + 10000000000000
            token_count += tokens_required(adx, ady, bdx, bdy, tx, ty)

    print(token_count)

solve()
