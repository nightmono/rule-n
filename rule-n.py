#!/usr/bin/python3

PATTERNS = (
    (1, 1, 1),
    (1, 1, 0),
    (1, 0, 1),
    (1, 0, 0),
    (0, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0)
)

def get_rule_set(rule):
    binary = bin(rule)[2:].zfill(8)
    return set(i for i in range(8) if binary[i] == "1")

def new_state(rule_set, l, m, r):
    for i in rule_set:
        if (l, m, r) == PATTERNS[i]:
            return 1
    return 0

def tick(cells, rule_set):
    next_gen = [0] * len(cells)
    
    for i in range(len(cells)):
        l = cells[i-1]
        m = cells[i]
        r = cells[(i+1)%len(cells)]

        next_gen[i] = new_state(rule_set, l, m, r)

    return next_gen

def main():
    import time
    import sys

    rule = 110
    cell_length = 60

    args = sys.argv
    for i, arg in enumerate(args):
        if arg == "--rule":
            rule = int(args[i+1]) 
        elif arg == "--length" or arg == "--len":
            cell_length = int(args[i+1])

    cells = [0] * cell_length
    cells[cell_length//2] = 1
    rule_set = get_rule_set(rule)
    print(rule_set)

    while 1:
        print("".join(map(str, cells)).replace("0", " ").replace("1", "#"))
        cells = tick(cells, rule_set)
        time.sleep(0.05)

if __name__ == "__main__":
    main()
