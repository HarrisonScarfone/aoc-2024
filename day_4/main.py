# FILEPATH = "day_4/test_input.txt"
FILEPATH = "day_4/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()




# # Part 1

def direction_offsets(i, j):
    return [
        [(i+1, j), (i+2, j), (i+3, j)],
        [(i-1, j), (i-2, j), (i-3, j)],
        [(i, j+1), (i, j+2), (i, j+3)],
        [(i, j-1), (i, j-2), (i, j-3)],
        [(i+1, j+1), (i+2, j+2), (i+3, j+3)],
        [(i-1, j+1), (i-2, j+2), (i-3, j+3)],
        [(i+1, j-1), (i+2, j-2), (i+3, j-3)],
        [(i-1, j-1), (i-2, j-2), (i-3, j-3)],
    ]
    

def find_xmas(arr, i, j, line):
    i1, j1 = line[0]
    i2, j2 = line[1]
    i3, j3 = line[2]
    if i3 >= len(arr) or i2 >= len(arr) or i1 >= len(arr):
        return False
    if j3 >= len(arr[0]) or j2 >= len(arr[0]) or j1 >= len(arr[0]):
        return False
    if i3 < 0 or i2 < 0 or i1 < 0 or j1 < 0 or j2 < 0 or j3 < 0:
        return False  
    if arr[i1][j1] == "M" and arr[i2][j2] == "A" and arr[i3][j3] == "S":
        return True
    
    return False

def solve():
    arr = [list(line.strip()) for line in read_input(FILEPATH)]
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "X":
                for offset in direction_offsets(i, j):
                    if find_xmas(arr, i, j, offset):
                        count += 1
                        a = 1

    print(count)
                

solve()

# Part 2

urdl = lambda arr, i, j : arr[i+1][j+1] == "M" and arr[i-1][j-1] == "S"
uldr = lambda arr, i, j : arr[i+1][j-1] == "M" and arr[i-1][j+1] == "S"
drul = lambda arr, i, j : arr[i-1][j+1] == "M" and arr[i+1][j-1] == "S"
dlur = lambda arr, i, j : arr[i-1][j-1] == "M" and arr[i+1][j+1] == "S"
    
def solve():
    arr = [list(line.strip()) for line in read_input(FILEPATH)]
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == "A":
                if i+1 >= len(arr) or i-1 < 0 or j+1 >= len(arr[0]) or j-1 < 0:
                    continue
                if uldr(arr, i, j) or drul(arr, i, j):
                    if urdl(arr, i, j) or dlur(arr, i, j):
                        count += 1

    print(count)
                

solve()