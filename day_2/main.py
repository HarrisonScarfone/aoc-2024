# FILEPATH = "day_2/test_input.txt"
FILEPATH = "day_2/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

# Part 1

# def solve():
#     safe_count = 0
#     for line in read_input(FILEPATH):
#         arr = [int(num) for num in line.split()]
#         arr = [(arr[i+1] - arr[i]) for i in range(len(arr) - 1)]
#         is_safe = True
#         if arr[0] > 0:
#             for elem in arr:
#                 if elem not in range(1,4):
#                     is_safe = False
#                     break
#         elif arr[0] < 0:
#             for elem in arr:
#                 if elem not in range(-3, 0):
#                     is_safe = False
#                     break
#         else:
#             is_safe = False

#         if is_safe:
#             safe_count += 1

#     print(safe_count)
        
# solve()



# Part 2

def solve():
    safe_count = 0
    for line in read_input(FILEPATH):
        arr = [int(num) for num in line.split()]

        diffs = []
        inc, dec = 0, 0
        for i in range(len(arr) - 2):
            diff1 = arr[i + 1] - arr[i]
            diff2 = arr[i + 2] - arr[i]
            if diff1 > 0:
                inc += 1
            else:
                dec += 1
            diffs.append((diff1, diff2))

        r = range(1, 4)
        if inc < dec:
            r = range(-3, 0)

        diffs.append((arr[-1] - arr[-2], r[-1]))
        count = 0
        idx = -1

        d1, d2 = diffs[0]
        if d1 not in r and d2 not in r:
            count += 1
            idx += 1

        while idx < len(diffs) - 1:
            idx += 1
            if diffs[idx][0] in r:
                continue
            elif diffs[idx][1] in r:
                count += 1
                if count > 1:
                    break
                idx += 1
            elif diffs[idx - 1][1] in r:
                    count += 1
                    continue
            else:
                count = 2
                break

        if count < 2:
            safe_count += 1

    print(safe_count)
        
solve()
