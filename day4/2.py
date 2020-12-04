#!/usr/bin/python3


import re
def solve():
    valid = 0
    with open('1.txt', 'r') as f:
        res = {
                'byr': '^(19[2-8][0-9]|199[0-9]|200[0-2])$',
                'iyr': '^(201[0-9]|2020)$',
                'eyr': '^(202[0-9]|2030)$',
                'hgt': '^(1[5-8][0-9]cm|19[0-3]cm)|(59in|6[0-9]in|7[0-6]in)$',
                'hcl': '^#[0-f]{6}$',
                'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
                'pid': '^\d{9}$',
        }
        passports = []
        temp = []
        valids = 0
        for line in f:
            if line == '\n':
                passports.append(temp)
                temp = []
            else:
                temp += [x for x in line.rstrip().split(' ')]
        passports.append(temp)
        for p in passports:
            print(p)
            s = ' '.join(p)
            if 'byr:' in s and 'iyr:' in s and 'eyr:' in s and \
            'hgt' in s and 'hcl:' in s and 'ecl:' in s and 'pid:' in s:
                valid = True
                for att in p:
                    k = att.split(':')[0]
                    v = att.split(':')[1]
                    if k == 'cid':
                        pass
                    else:
                        if not re.match(res[k], v):
                            valid = False
                if valid:
                    valids += 1
    return valids


print(solve())
