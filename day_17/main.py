# FILEPATH = "day_17/test_input.txt"
FILEPATH = "day_17/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()
    

# Part 1

def run_computer(registers, program):
    ra, rb, rc = registers
    pc = 0
    output = ""

    while pc < len(program):
        opcode = program[pc]
        preoperand = program[pc+1]

        operand = None
        if preoperand < 4:
            operand = preoperand
        elif preoperand == 4:
            operand = ra
        elif preoperand == 5:
            operand = rb
        elif preoperand == 6:
            operand == rc
        else:
            raise ValueError

        if opcode == 0:
            ra = ra // (2**operand)
        elif opcode == 1:
            rb = rb ^ preoperand
        elif opcode == 2:
            rb = operand % 8
        elif opcode == 3:
            if ra != 0:
                pc = preoperand
                continue
        elif opcode == 4:
            rb = rb ^ rc
        elif opcode == 5:
            output += f"{operand % 8},"
        elif opcode == 6:
            rb = ra // (2**operand)
        elif opcode == 7:
            rc = ra // (2**operand)

        pc += 2

    return output[:-1]

def solve():
    program = []
    registers = []
    for line in read_input(FILEPATH):
        if line.startswith("R"):
            registers.append(int(line.strip().split(":")[-1].strip()))
        if line.startswith("Program:"):
            program = [int(x) for x in line.strip().split(":")[-1].split(",")]

    target = ",".join([str(x) for x in program])

    def find_3_nums(target, curr):
        result = []
        for i in range(8):
            for j in range(8):
                for k in range(8):
                    for val in curr:
                        registers[0] = int(f"{val}{i}{j}{k}", 8)
                        curr_result = run_computer(registers, program)
                        if curr_result == target:
                            result.append(f"{val}{i}{j}{k}")
        return result

    r1 = find_3_nums("5,3,0", " ")
    # print(r1)
    r2 = find_3_nums("0,3,5,5,3,0", r1)
    # print(r2)
    r3 = find_3_nums("3,1,6,0,3,5,5,3,0", r2)
    # print(r3)
    r4 = find_3_nums("7,5,4,3,1,6,0,3,5,5,3,0", r3)
    # print(r4)
    r5 = find_3_nums("4,1,5,7,5,4,3,1,6,0,3,5,5,3,0", r4)
    print(sorted(r5))

    # The just guess at the last number, it goes in the lsb position

    registers[0] = int("3002511352304632", 8)
    print(registers[0])
    print(run_computer(registers, program))

solve()

