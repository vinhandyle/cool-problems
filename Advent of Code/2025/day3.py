# Day 3: Lobby
# Part 1: 16854
# Part 2: 167526011932478

import lib

def run():
    banks = process_input()
    
    tot = 0
    for b in banks:
        mx, j = 0, int(b[0])
        for i in range(1, len(b)):
            k = int(b[i])
            mx = max(mx, j * 10 + k)
            if i < len(b) - 1:
                j = max(j, k)
        tot += mx
    print(tot)
    
    tot, turns = 0, 12
    for b in banks:
        arr = []
        for i in range(turns):
            arr.append(max(b[:len(b) - turns + i + 1]))
            b = b[b.index(arr[i]) + 1:]
        mx = int(''.join(arr))
        tot += mx
    print(tot)



def process_input():
    input = lib.read_input('input3.txt')
    return input



if __name__ == '__main__':
    run()