# Day 2: Gift Shop
# Part 1: 18700015741
# Part 2: 20077272987

import lib
import re

def run():
    ranges = process_input()

    pattern, tot = r'^(?P<g>[1-9]\d*)(?P=g)$', 0
    for r in ranges:
        for i in range(r[0], r[1]+1):
            if re.match(pattern, str(i)):
                tot += i
    print(tot)

    pattern, tot = r'^(?P<g>[1-9]\d*)(?P=g)+$', 0
    for r in ranges:
        for i in range(r[0], r[1]+1):
            if re.match(pattern, str(i)):
                tot += i
    print(tot)



def process_input():
    input = lib.read_input('input2.txt')
    return list((int(s.split('-')[0]), int(s.split('-')[1])) for s in input[0].split(','))



if __name__ == '__main__':
    run()