#!/usr/bin/python3


def solve():
    with open('1.txt', 'r') as f:
        total = 0
        temp = ''
        for line in f:
            if line == '\n':
                total += len(temp)
                temp = ''
            else:
                for c in line.rstrip():
                    if c not in temp:
                        temp += c
    return total




print(solve())
