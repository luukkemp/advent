#!/usr/bin/python3

def solve():
    inputs = []
    total = 0
    with open('1.txt', 'r') as f:
        for line in f:
            try:
                s = line.split(' ')
                minimum = int(s[0].split('-')[0])
                maximum = int(s[0].split('-')[1])
                char = s[1].split(':')[0]
                passw = s[2]
                print(minimum, maximum, char, passw)
                count = 0
                for c in passw:
                    if c == char:
                        count += 1
                if minimum <= count <= maximum:
                    total += 1
            except:
                pass
    return total

print(solve())
