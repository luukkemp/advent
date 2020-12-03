#!/usr/bin/python3



def solve():
    answers = [2020]
    numbers = []
    with open('1.txt', 'r') as f:
        for line in f:
            try:
                numbers.append(int(line.rstrip('\n')))
            except:
                pass
    for n in numbers:
        for nn in numbers:
            if n + nn in answers:
                return n * nn
print(solve())
