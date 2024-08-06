#!/usr/bin/python3

patterns = (
    (1, 1, 1),
    (1, 1, 0),
    (1, 0, 1),
    (1, 0, 0),
    (0, 1, 1),
    (0, 1, 0),
    (0, 0, 1),
    (0, 0, 0)
)

def rule30(l, m, r):
    for i in (3, 4, 5, 6):
        if (l, m, r) == patterns[i]:
            return 1
    return 0

def tick(cells):
    next_gen = [0] * len(cells)
    
    for i in range(len(cells)):
        l = cells[i-1]
        m = cells[i]
        r = cells[(i+1)%len(cells)]

        next_gen[i] = rule30(l, m, r)

    return next_gen

import time

cells = [0] * 60
cells[len(cells)//2] = 1

while 1:
    print("".join(map(str, cells)).replace("0", " ").replace("1", "#"))
    cells = tick(cells)
    time.sleep(0.1)
