FILEPATH = "day_10/test_input.txt"
# FILEPATH = "day_10/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()
    

# # Part 1

# not_in_bounds = lambda arr, i, j : i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0])

# def count_paths(arr, i, j, last_elevation, seen):
#     if not_in_bounds(arr, i, j):
#         return 0
#     val = arr[i][j]
#     if val != last_elevation + 1:
#         return 0
#     if val == 9:
#         if (i, j) not in seen:
#             seen.add((i, j))
#             return 1
#         else:
#             return 0

#     return (count_paths(arr, i+1, j, val, seen) +
#             count_paths(arr, i, j+1, val, seen) + 
#             count_paths(arr, i-1, j, val, seen) +
#             count_paths(arr, i, j-1, val, seen))
        
# def count_trailheads(arr):
#     trailhead_count = 0
#     for i in range(len(arr)):
#         for j in range(len(arr)):
#             if arr[i][j] == 0:
#                 trailhead_count += count_paths(arr, i, j, -1, set())
    
#     return trailhead_count

# def solve():
#     arr = []
#     for line in read_input(FILEPATH):
#         arr.append([int(val) if val != "." else -1 for val in list(line.strip())])

#     trailhead_count = count_trailheads(arr)
#     print(trailhead_count)

# solve()

# Part 2

not_in_bounds = lambda arr, i, j : i < 0 or j < 0 or i >= len(arr) or j >= len(arr[0])

def count_paths(arr, i, j, last_elevation, seen):
    if not_in_bounds(arr, i, j):
        return 0
    val = arr[i][j]
    if val != last_elevation + 1:
        return 0
    if val == 9:
        return 1

    return (count_paths(arr, i+1, j, val, seen) +
            count_paths(arr, i, j+1, val, seen) + 
            count_paths(arr, i-1, j, val, seen) +
            count_paths(arr, i, j-1, val, seen))
        
def count_trailheads(arr):
    trailhead_count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                trailhead_count += count_paths(arr, i, j, -1, set())
    
    return trailhead_count

def solve():
    arr = []
    for line in read_input(FILEPATH):
        arr.append([int(val) if val != "." else -1 for val in list(line.strip())])

    trailhead_count = count_trailheads(arr)
    print(trailhead_count)

solve()