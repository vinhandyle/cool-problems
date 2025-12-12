# Day 6: Trash Compactor
# Part 1: 4722948564882
# Part 2: 9581313737063

import lib

def run():
    ps, tot = process_input(), 0
    for p in ps:
        tot += eval(p[-1].join(p[:-1]))
    print(tot)

    ps, tot = process_input2(), 0
    for p in ps:
        tot += eval(p[-1].join(p[:-1]))
    print(tot)



def process_input():
    input = lib.read_input('input6.txt')
    temp = list(list(filter(lambda x: x != '', list(w.strip() for w in line.split(' ')))) for line in input)
    
    ps = []
    for i in range(len(temp[0])):
        p = []
        for j in range(len(temp)):
            p.append(temp[j][i])
        ps.append(p)
    return ps



def process_input2():
    input = lib.read_input('input6.txt')
    
    # Build numbers top-to-bottom
    temp = []
    for line in input:
        for i in range(len(line)):
            if len(temp) < i + 1:
                temp.append([])
            temp[i] += line[i]

    # Group into problems
    temp, p, ps = list(''.join(w).strip() for w in temp), [], []
    temp.append('')
    for w in temp:
        if w == '':
            p.append(p[0][-1])
            p[0] = p[0][:-1].strip()
            ps.append(p)
            p = []
        else:
            p.append(w)
    return ps



if __name__ == '__main__':
    run()