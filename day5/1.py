#!/usr/bin/python3


def str_to_bin(s):
    b = ''
    table = {
            'F': '0',
            'B': '1',
            'L': '0',
            'R': '1'
    }
    for c in s:
        b += table[c]
    return (int(b[:7], 2), int(b[7:], 2))

def solve():
    ids = []
    with open('1.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            row, column  =  str_to_bin(line)
            ids.append(row*8 + column)
    ids.sort()
    return ids.pop()



print(solve())
