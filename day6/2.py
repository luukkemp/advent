#!/usr/bin/python3


def solve():
    with open('1.txt', 'r') as f:
        total = 0
        temp = []
        counter = 0
        for line in f:
            if line == '\n':
                tempset = dict.fromkeys(temp, 0)
                for c in temp:
                    tempset[c] += 1
                for key in tempset:
                    if tempset[key] == counter:
                        total += 1
                temp = []
                counter = 0
            else:
                counter += 1
                for c in line.rstrip():
                    temp.append(c)
    return total




print(solve())
