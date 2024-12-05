# FILEPATH = "day_5/test_input.txt"
FILEPATH = "day_5/input.txt"

def read_input(filepath):
    with open(filepath, "r") as f:
        return f.readlines()

# Part 1

def validate_order(rules, order):
    bad = set()
    for elem in reversed(order):
        if elem in bad:
            return False
        for val in rules.get(elem, []):
            bad.add(val)
    return True

# def solve():
#     rules = {}
#     orders = []
#     section2 = False
#     for line in read_input(FILEPATH):
#         line = line[:-1]
#         if line == '-----':
#             section2 = True
#             continue
#         if not section2:
#             k, v = line.split("|")
#             rules[k] = rules.get(k, []) + [v]
#             continue
#         orders.append(line.strip().split(","))

#     count = 0
#     for order in orders:
#         if validate_order(rules, order):
#             count += int(order[len(order)//2])

#     print(count)

# solve()

from graphlib import TopologicalSorter
from collections import defaultdict

# Part 2

def valid_order(rules):
    ts = TopologicalSorter(rules)
    return list(ts.static_order())[::-1]

def solve():
    rules = {}
    orders = []
    section2 = False
    for line in read_input(FILEPATH):
        line = line[:-1]
        if line == '-----':
            section2 = True
            continue
        if not section2:
            k, v = line.split("|")
            rules[k] = rules.get(k, []) + [v]
            rules[k] = list(set(rules[k]))
            continue
        orders.append(line.strip().split(","))

    count = 0
    for order in orders:
        subgraph = defaultdict()
        for k in order:
            if k in rules:
                subgraph[k] = [n for n in rules[k] if n in order]
            else:
                subgraph[k] = []

        v = valid_order(subgraph)
        if order != v:
            count += int(v[len(v)//2])

    print(count)

solve()
