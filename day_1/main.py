# FILEPATH = "day_1/test_input.txt"
FILEPATH = "day_1/input.txt"

# Part 1

# def read_input(filepath):
#     with open(filepath, "r") as f:
#         return f.readlines()

# def solve():
#     left, right = [], []
#     for line in read_input(FILEPATH):
#         coordinates = line.split()
#         left.append(int(coordinates[0]))
#         right.append(int(coordinates[1]))
    
#     left.sort()
#     right.sort()

#     distance = 0

#     for l, r in zip(left, right):
#         distance += abs(l - r)

#     print(distance)

# solve()


# Part 2

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

def solve():
    left, right = set(), {}
    for line in read_input(FILEPATH):
        coordinates = line.split()
        l, r = coordinates
        left.add(int(l))
        r = int(r)
        right[r] = right.get(r, 0) + 1

    distance = 0
    for elem in left:
        if elem in right:
            distance += elem * right[elem]

    print(distance)

solve()
