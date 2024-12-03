# FILEPATH = "day_3/test_input.txt"
FILEPATH = "day_3/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


import re

# Part 1

# def solve():
#     pattern = r"mul\((\d+,\d+)\)"
#     sum = 0
#     for line in read_input(FILEPATH):
#         muls = [item.split(",") for item in re.findall(pattern, line)]
#         muls = [(int(item[0]), int(item[1])) for item in muls]
#         for mul in muls:
#             sum += mul[0] * mul[1]

#     return sum

# solve()


# Part 2

def solve1(line):
    pattern = r"mul\((\d+,\d+)\)"
    sum = 0
    muls = [item.split(",") for item in re.findall(pattern, line)]
    muls = [(int(item[0]), int(item[1])) for item in muls]
    for mul in muls:
        sum += mul[0] * mul[1]
    return sum

def solve2():
    count = 0
    doing = True
    with open(FILEPATH, "r") as f:
        line = f.read()       
        while line:
            if doing:
                idx = line.find("don\'t()")
                count += solve1(line[:idx])
            else:
                idx = line.find("do()")
            if idx == -1:
                break
            line = line[idx:]
            doing = not doing
        if doing:
            count += solve1(line)

    print(count)

solve2()
