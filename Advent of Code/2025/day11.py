# Day 11: Reactor
# Part 1: 494
# Part 2: 

import lib

def run():
    d = process_input()
    
    paths = get_paths(d, 'you', 'out')
    print(len(paths))

    p1 = get_paths(d, 'fft', 'out')
    p2 = get_paths(d, 'dac', 'out')
    print(len(p1), len(p2))



def get_paths(d, start, end):
    paths, frontier = [], [[start]]
    while len(frontier) > 0:
        p = frontier.pop(0)
        for nxt in d[p[-1]]:
            if nxt not in p:
                if nxt == end:
                    paths.append(p + [nxt])
                elif nxt != 'out':
                    frontier.append(p + [nxt])
    return paths



def process_input():
    input = lib.read_input('input11.txt')
    d = dict()
    for line in input:
        x, y = line.split(':')
        d[x] = y.strip().split(' ')
    return d



if __name__ == '__main__':
    run()