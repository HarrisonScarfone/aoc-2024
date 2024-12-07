FILEPATH = "day_7/test_input.txt"
# FILEPATH = "day_7/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()


# Part 1

# def get_val(a, b, operation):
#     if operation == "+":
#         return a + b
#     elif operation == "*":
#         return a * b

# def calculate_val(operands, operators):
#     result = get_val(operands[0], operands[1], operators[0])

#     for i in range(1, len(operators)):
#         result = get_val(result, operands[i+1], operators[i]) 

#     return result

# def can_make_target(target, operands, operators):
#     if len(operators) == len(operands) - 1:
#         val = calculate_val(operands, operators)
#         return val == target
    
#     return (can_make_target(target, operands, operators+["+"]) or
#             can_make_target(target, operands, operators+["*"]))

# def solve():
#     total = 0
#     for line in read_input(FILEPATH):
#         elements = line.split()
#         target = int(elements[0][:-1])
#         operands = [int(elem) for elem in elements[1:]]

#         if can_make_target(target, operands, []):
#             total += target

#     print(total)

# solve()

# Part 2

def get_val(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "*":
        return a * b
    elif operation == "||":
        return int(str(a) + str(b))

def calculate_val(operands, operators):
    result = get_val(operands[0], operands[1], operators[0])

    for i in range(1, len(operators)):
        result = get_val(result, operands[i+1], operators[i]) 

    return result

def can_make_target(target, operands, operators):
    if len(operators) == len(operands) - 1:
        val = calculate_val(operands, operators)
        return val == target
    
    return (can_make_target(target, operands, operators+["+"]) or
            can_make_target(target, operands, operators+["*"]) or
            can_make_target(target, operands, operators+["||"]))

def solve():
    total = 0
    for line in read_input(FILEPATH):
        elements = line.split()
        target = int(elements[0][:-1])
        operands = [int(elem) for elem in elements[1:]]

        if can_make_target(target, operands, []):
            total += target

    print(total)

solve()