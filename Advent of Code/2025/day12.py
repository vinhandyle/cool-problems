# Day 12: Christmas Tree Farm
# Part 1: 
# Part 2: 

import lib
import re

def run():
    shapes, trees = process_input()

    tot = 0
    for tree, reqs in trees:
        if fit_shapes(tree, shapes, reqs):
            tot += 1
    print(tot)

    

def fit_shapes(tree, shapes, reqs):
    return True



def process_input():
    input = lib.read_input('input12.txt')
    shapes, trees = [], []
    for line in input:
        if line.strip() != '':
            if 'x' in line:
                pattern = r'(\d+)x(\d+): (.+)'
                m = re.search(pattern, line)
                trees.append(((int(m.group(1)), int(m.group(2))), list(int(i) for i in m.group(3).split(' '))))
            elif line[1].rstrip()[-1] == ':':
                shapes.append([])
            else:
                shapes[-1].append(line)
    return shapes, trees



if __name__ == '__main__':
    run()