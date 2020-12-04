#!/usr/bin/python3


def solve():
    valid = 0
    with open('1.txt', 'r') as f:
        passports = []
        temp = ''
        for line in f:
            if line == '\n':
                passports.append(temp)
                temp = ''
            else:
                temp += line.rstrip()
        for p in passports:
            if 'byr:' in p and 'iyr:' in p and 'eyr:' in p and \
            'hgt' in p and 'hcl:' in p and 'ecl:' in p and 'pid:' in p:
                valid += 1
    return valid


print(solve())
