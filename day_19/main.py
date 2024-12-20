# FILEPATH = "day_19/test_input.txt"
FILEPATH = "day_19/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()
    

# Part 1 and 2 (swap the count on 33 to += 1 for p1)

import functools

class DesignChecker:
    def __init__(self, pieces):
        self.pieces = set(pieces)

    @functools.lru_cache
    def can_make_design(self, target):
        makeable = 0
        for piece in self.pieces:
            if target.startswith(piece):
                if len(target) == len(piece):
                    makeable += 1
                else:
                    makeable += self.can_make_design(str(target[len(piece):]))
        return makeable     

def make_new_towels(pieces, designs):
    count = 0
    dc = DesignChecker(pieces)
    for design in designs:
        if result := dc.can_make_design(design):
            count += result
    return count

def solve():
    pieces = []
    designs = []

    for i, line in enumerate(read_input(FILEPATH)):
        if i == 0:
            pieces = [x.strip() for x in line.strip().split(",")]
            continue
        elif i == 1:
            continue
        designs.append(line.strip())

    print(make_new_towels(pieces, designs))
    

solve()
