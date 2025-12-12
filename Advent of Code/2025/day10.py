# Day 10: Factory
# Part 1: 457
# Part 2: 

import lib
import re
import numpy as np

def run():
    machines = process_input()
    
    tot = 0
    for m in machines:
        tot += turn_on_dp(m[1], m[0])
    print(tot)

    # under 17901
    tot = 0
    for m in machines:
        tot += set_joltage(m[1], m[2])
    print(tot)



# O(n)
def set_joltage(buttons, reqs):
    A, b = [], np.matrix(reqs).transpose()
    for btn in buttons:
        col = list(0 for _ in range(len(reqs)))
        for p in btn:
            col[p] = 1
        A.append(col)
    A = np.matrix(A).transpose()
    x = np.linalg.lstsq(A, b)[0]
    return sum(round(x[i,0]) for i in range(len(x)))



# O(knm), where k is max joltage
def set_joltage_dp(buttons, reqs):
    d = {tuple(0 for _ in reqs): 0}
    frontier = list(d.keys())
    while len(frontier) > 0:
        state, bad = frontier.pop(0), False
        for b in buttons:
            temp = list(state)
            for p in b:
                temp[p] += 1
                if temp[p] > reqs[p]:
                    bad = True
            if not bad and (k := tuple(temp)) not in d:
                d[k] = d[state] + 1
                frontier.append(k)
    return d[tuple(reqs)]



# O(nm)
def turn_on_dp(buttons, lights):
    d = {tuple(False for _ in lights): 0}
    frontier = list(d.keys())
    while len(frontier) > 0:
        state = frontier.pop(0)
        for b in buttons:
            temp = list(state)
            for p in b:
                temp[p] = not temp[p]
            if (k := tuple(temp)) not in d:
                d[k] = d[state] + 1
                frontier.append(k)
    return d[tuple(lights)]



# Brute force using BST (way too slow)
def turn_on_bf(lights, buttons):
    q = list((i, [False] * len(lights), [buttons[i]]) for i in range(len(buttons)))
    while True:
        i, state, hist = q.pop(0)
        for j in buttons[i]:
            state[j] = not state[j]
        if state == lights:
            #print(hist)
            return len(hist)
        elif any(state == _state and len(hist) >= len(_hist) for _, _state, _hist in q):
            continue
        else:
            for j in range(len(buttons)):
                q.append((j, list(state), hist + [buttons[j]]))



def process_input():
    input = lib.read_input('input10.txt')
    machines, pattern = [], r'\[(.+)\] (.+) \{(.+)\}'
    for line in input:
        m = re.search(pattern, line)
        x = list(s == '#' for s in m.group(1))
        y = list(eval(f'[{s[1:-1]}]') for s in m.group(2).split(' '))
        z = list(int(s) for s in m.group(3).split(','))
        machines.append((x, y, z))
    return machines



if __name__ == '__main__':
    run()