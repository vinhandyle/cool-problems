# Day 7: Laboratories
# Part 1: 1598
# Part 2: 

from collections import defaultdict

import lib

def run():
    start, splitters = process_input()
   
    tree, f_beams = defaultdict(int), dict()
    tree[start] = 1

    beams, splits = {start}, set()
    while len(beams) > 0:
        temp = set()
        for b in beams:
            if n_splitters := sorted(filter(lambda s: s[0] > b[0] and s[1] == b[1], splitters)):
                s = n_splitters[0]
                temp.add((s[0], s[1] - 1))
                temp.add((s[0], s[1] + 1))
                tree[(s[0], s[1] - 1)] += tree[b]
                tree[(s[0], s[1] + 1)] += tree[b]
                splits.add(s)
            else:
                f_beams[b] = tree[b]
        beams = temp
    print(len(splits))
    #print('\n'.join(str(i) for i in f_beams.items()))
    print(sum(t for t in f_beams.values())) # under 5891269782251362111579



def process_input():
    input = lib.read_input('input7.txt')
    start, splitters = None, []
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == 'S':
                start = (i, j)
            elif input[i][j] == '^':
                splitters.append((i, j))
    return start, splitters



if __name__ == '__main__':
    run()