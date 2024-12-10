# FILEPATH = "day_9/test_input.txt"
FILEPATH = "day_9/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()
    

# Part 1

# def get_l_idx(disk, ptr):
#     while disk[ptr] != "." and ptr < len(disk) - 1:
#         ptr += 1
#     return ptr

# def get_r_idx(disk, ptr):
#     while disk[ptr] == "." and ptr > -1:
#         ptr -= 1
#     return ptr

# def rearrange_disk(disk):
#     l = get_l_idx(disk, 0)
#     r = get_r_idx(disk, len(disk) - 1)

#     while l < r:
#         disk[l], disk[r] = disk[r], disk[l]
#         l = get_l_idx(disk, l)
#         r = get_r_idx(disk, r)

# def get_checksum(disk):
#     checksum = 0
#     for i, elem in enumerate(disk):
#         checksum += i * elem if elem != "." else 0
#     return checksum

# def solve():
#     raw_disk = None
#     for line in read_input(FILEPATH):
#         raw_disk = line.strip()

#     disk = []
#     curr_id = 0
#     is_empty_space = False
#     for char in raw_disk:
#         num = int(char)
#         if is_empty_space:
#             disk += ['.'] * num
#         else:
#             disk += [curr_id] * num
#             curr_id += 1
#         is_empty_space = not is_empty_space

#     rearrange_disk(disk)
#     checksum = get_checksum(disk)
    
#     print(checksum)

# solve()

# Part 2

def rearrange_disk(disk):
    to_swap = []
    last = disk[-2]
    count = 0
    for elem in reversed(disk):
        if elem == "." or elem == "/":
            continue
        if elem == last:
            count += 1
        else:
            to_swap.append((last, count))
            last = elem
            count = 1

    disk_str = "".join([str(x) for x in disk])

    for swap in to_swap:
        id, space_needed= swap
        target_string = "./" * space_needed
        replace_string = f"{id}/" * space_needed
        tidx = disk_str.find(target_string)
        ridx = disk_str.find(replace_string)
        if tidx > -1 and tidx <= ridx:
            disk_str = disk_str.replace(replace_string, target_string, 1) 
            disk_str = disk_str.replace(target_string, replace_string, 1)

    return disk_str

def get_checksum(disk):
    checksum = 0
    for i, elem in enumerate(disk):
        if elem != ".":
            checksum += i * int(elem)
    return checksum

def solve():
    raw_disk = None
    for line in read_input(FILEPATH):
        raw_disk = line.strip()

    disk = []
    curr_id = 0
    is_empty_space = False
    for char in raw_disk:
        num = int(char)
        if is_empty_space:
            disk += ['.', '/'] * num
        else:
            disk += [curr_id, "/"] * num
            curr_id += 1
        is_empty_space = not is_empty_space

    disk_str = rearrange_disk(disk)
    disk = disk_str.split("/")[:-1]
    checksum = get_checksum(disk)
    
    print(checksum)

solve()
