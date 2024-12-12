# FILEPATH = "day_11/test_input.txt"
FILEPATH = "day_11/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

# Part 1/2
import time

rule1 = lambda x : ["1"] if x == "0" else []
rule2 = lambda x : [x[:len(x)//2], str(int(x[len(x)//2:]))] if not len(x) % 2 else []
rule3 = lambda x : [str(int(x) * 2024)]
apply_rules = lambda x : rule1(x) or rule2(x) or rule3(x)

def solve():
    arr = ""
    with open(FILEPATH, "r") as f:
        arr = f.read().split()

    BLINKS = 75
    start_time = time.time()
    
    last_layer = {}
    for elem in arr:
        last_layer[elem] = last_layer.get(elem, 0) + 1

    curr_layer = {}
    layers_to_process = BLINKS
    
    while layers_to_process > 0:
        for key in last_layer.keys():
            blink_result = apply_rules(key)
            for elem in blink_result:
                curr_layer[elem] = curr_layer.get(elem, 0) + last_layer[key]
        
        last_layer = curr_layer
        curr_layer = {}
        layers_to_process -= 1

    leaf_count = sum(last_layer[key] for key in last_layer)

    total_time = time.time() - start_time 
    print(f"Took {total_time} seconds.")
    print(leaf_count)     
    
solve()
