# Day 5: Cafeteria
# Part 1: 811
# Part 2: 338189277144473

import lib

def run():
    ranges, ings = process_input()
    ranges = sorted(ranges)
    
    fresh = 0
    for i in ings:
        for r in ranges:
            if i >= r[0] and i <= r[1]:
                fresh += 1
                break
    print(fresh)

    merged = [ranges[0]]
    for r in ranges[1:]:
        diff = add_to_pool(merged, r)
        while diff:
            temp, diff = [merged[0]], False
            for mr in merged[1:]:
                diff = diff or add_to_pool(temp, mr)
            merged = temp
        merged = sorted(merged)
    
    fresh = 0
    for r in sorted(merged):
        fresh += r[1] - r[0] + 1
    print(fresh)



def add_to_pool(pools, np):
    diff, subset = False, False
    for p in pools:
        # Extend lower bound
        if np[1] + 1 == p[0] or \
            (np[0] < p[0] and np[1] >= p[0] and np[1] <= p[1]):
            p[0] = np[0]
            diff = True
        # Extend upper bound
        if np[0] - 1 == p[1] or \
            (np[1] > p[1] and np[0] <= p[1] and np[0] >= p[0]):
            p[1] = np[1]
            diff = True
        # Superset
        if np[0] < p[0] and np[1] > p[1]:
            p[0] = np[0]
            p[1] = np[1]
            diff = True
        subset = np[0] >= p[0] and np[1] <= p[1]
    if not diff and not subset and np not in pools:
        pools.append(np)
    return diff



def process_input():
    input = lib.read_input('input5.txt')
    ranges, ings, switch = [], [], False
    for line in input:
        if switch:
            ings.append(int(line))
        else:
            if line == '':
                switch = True
            else:
                ranges.append(list(int(s) for s in line.split('-')))
    return ranges, ings



if __name__ == '__main__':
    run()