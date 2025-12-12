# Day 1: Secret Entrance
# Part 1: 1177
# Part 2: 6768

import lib

def run():
    rots = process_input()  
    d = 100

    n, z = 50, 0
    for r in rots:
        n = (n + r) % d
        z += 1 if n == 0 else 0
    print(z)

    n, z = 50, 0
    for r in rots:
        z += abs(r) // d                                            # Complete rotations
        r = (-1 if r < 0 else 1) * (abs(r) % d)
        z += 1 if (n * r != 0) and (n + r > d or n + r < 0) else 0  # Cross-overs
        n = (n + r) % d
        z += 1 if n == 0 else 0                                     # Perfect landings
    print(z)



def process_input():
    input = lib.read_input('input1.txt')
    for i in range(len(input)):
        input[i] = (-1 if input[i][0] == 'L' else 1) * int(input[i][1:])
    return input



if __name__ == '__main__':
    run()