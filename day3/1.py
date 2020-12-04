#!/usr/bin/python3


def virtual_x(x_len, x):
    return x % x_len

def solve(x, y):
    inputs = []
    posx = 0
    posy = 0
    trees = 0
    with open('1.txt', 'r') as f:
        m = []
        for line in f:
            m.append([x for x in line.rstrip()])
        y_len = len(m)
        x_len = len(m[0])
        while posy < y_len:
            if m[posy][virtual_x(x_len, posx)] == '#':
                trees += 1
            posy += y
            posx += x
    return trees


print(solve(3,1))
