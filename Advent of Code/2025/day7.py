# Day 7: Laboratories
# Part 1: 1598
# Part 2: 4509723641302

from collections import defaultdict

import lib

def run():
    start, splitters = process_input()
    tree = defaultdict(set)

    beams, splits = {start}, set()
    while len(beams) > 0:
        temp = set()
        for b in beams:
            if n_splitters := sorted(filter(lambda s: s[0] > b[0] and s[1] == b[1], splitters)):
                s = n_splitters[0]
                l, r = (s[0], s[1] - 1), (s[0], s[1] + 1)
                tree[b] = {l, r}
                temp |= tree[b]
                splits.add(s)
        beams = temp
    print(len(splits))

    dp = dict()
    def get_timelines(node):
        v = 1
        if node in dp:
            return dp[node]
        if len(tree[node]) > 0:
            v = sum(get_timelines(split) for split in tree[node])
        dp[node] = v
        return v
    print(get_timelines(start))
    


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