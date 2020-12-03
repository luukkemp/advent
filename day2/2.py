#!/usr/bin/python3


def solve():
    inputs = []
    total = 0
    with open('1.txt', 'r') as f:
        for line in f:
            s = line.split(' ')
            n1 = int(s[0].split('-')[0])
            n2 = int(s[0].split('-')[1])
            char = s[1].split(':')[0]
            passw = s[2]
            count = 0
            if passw[n1-1] == char:
                count += 1
            if passw[n2-1] == char:
                count += 1
            if count == 1:
                total += 1
            print(count)
    return total

print(solve())
