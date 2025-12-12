# Day 8: Playground
# Part 1: 244188
# Part 2: 8361881885

import lib

def run():
    boxes = process_input()
    
    dist_map = dict()
    for ba in boxes:
        for bb in boxes:
            if ba != bb and (bb, ba) not in dist_map:
                dist_map[(ba, bb)] = get_dist(ba, bb)                   
    
    dist_list = sorted(list((k[0], k[1], v) for k, v in dist_map.items()), key = lambda x: x[2])
    
    conns = mst(dist_list, 1000)   
    conn_sizes, ans = sorted(list(len(c) for c in conns), reverse=True), 1
    for i in range(3):
        ans *= conn_sizes[i]
    print(ans)

    ans = mst(dist_list, len(dist_list), len(boxes))
    print(ans)



def get_dist(o, t):
    dx = t[0] - o[0]
    dy = t[1] - o[1]
    dz = t[2] - o[2]
    return (dx**2 + dy**2 + dz**2) ** (1/2)



def mst(dist_list, iters, box_cnt = -1):
    conns = []
    for i in range(iters):
        b1, b2, _ = dist_list[i]
        targets = list(filter(lambda x: b1 in x or b2 in x, conns))
        if len(targets) > 0:
            merge = {b1, b2}
            for s in targets:
                merge |= s
                conns.remove(s)
            conns.append(merge)
        else:
            conns.append({b1, b2})
        if len(conns[0]) == box_cnt:
            return b1[0] * b2[0]
    return conns



def process_input():
    input = lib.read_input('input8.txt')
    arr = []
    for line in input:
        arr.append(eval(f'({line})'))
    return arr



if __name__ == '__main__':
    run()