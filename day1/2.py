#!/usr/bin/python3
import random

def solve():
    answer = 2020
    n = []
    with open('1.txt', 'r') as f:
        for line in f:
            try:
                n.append(int(line.rstrip('\n')))
            except:
                pass
    guess = 0
    while guess != answer:
        r1 = random.randint(0, len(n) - 1)
        r2 = random.randint(0, len(n) - 1)
        r3 = random.randint(0, len(n) - 1)
        guess = n[r1] + n[r2] + n[r3]
    return n[r1] * n[r2] * n[r3]


print(solve())
