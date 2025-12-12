# Day 9: Movie Theater
# Part 1: 4782896435
# Part 2: 

import lib

def run():
    corners = process_input()

    ans = max(get_rect_area(c1, c2) for c1 in corners for c2 in corners)
    print(ans)

    border, prev = set(), corners[-1]
    for c in corners:
        border |= get_line(c, prev)
        prev = c   
    #print_grid((max(c[0] for c in border)+3, max(c[1] for c in border)+2), border)

    # For quick border check later
    x, y = dict(), dict()
    for b in border:
        if b[1] not in x:
            x[b[1]] = (b[0], b[0])
        if b[0] not in y:
            y[b[0]] = (b[1], b[1])
        minx, maxx = x[b[1]]
        miny, maxy = y[b[0]]
        x[b[1]] = (min(minx, b[0]), max(maxx, b[0]))
        y[b[0]] = (min(miny, b[1]), max(maxy, b[1]))

    # 511272 < ans < 4577617116
    mx = 0
    for c1 in corners:
        for c2 in corners:
            hc = [
                (c1[0], c2[1]), \
                (c2[0], c1[1]), \
                (c1[0], (c1[1] + c2[1]) // 2), \
                (c2[0], (c1[1] + c2[1]) // 2), \
                ((c1[0] + c2[0]) // 2, c1[1]), \
                ((c1[0] + c2[0]) // 2, c2[1])
            ]
            if all(within_border(x, y, c) for c in hc):
                if not any(min(c1[0], c2[0]) < c[0] < max(c1[0], c2[0]) \
                    and min(c1[1], c2[1]) < c[1] < max(c1[1], c2[1]) for c in corners):
                    mx = max(mx, get_rect_area(c1, c2))
                    if mx == get_rect_area(c1, c2):
                       print(c1, c2, mx)
    print(mx)



def get_rect_area(c1, c2):
    return abs(c2[0] - c1[0] + 1) * abs(c2[1] - c1[1] + 1)



def get_line(c1, c2):
    line = set()
    if c1[0] < c2[0]:
        for i in range(c1[0], c2[0]+1):
            line.add((i, c1[1]))
    elif c1[0] > c2[0]:
        for i in range(c2[0], c1[0]):
            line.add((i, c1[1]))
    elif c1[1] < c2[1]:
        for i in range(c1[1], c2[1]+1):
            line.add((c1[0], i))
    elif c1[1] > c2[1]:
        for i in range(c2[1], c1[1]):
            line.add((c1[0], i))
    return line



def within_border(x, y, c):
    # Does not correctly handle point outside of border but physically enclosed
    return c[1] in x and c[0] in y \
        and x[c[1]][0] <= c[0] <= x[c[1]][1] \
        and y[c[0]][0] <= c[1] <= y[c[0]][1]



def print_grid(size, border):
    grid = list(['.'] * size[0] for _ in range(size[1]))
    for c in border:
        grid[c[1]][c[0]] = 'X'
    with open('print9.txt', 'w') as f:
        for row in grid:
            for cell in row:
                f.write(cell)
            f.write('\n')



def process_input():
    input = lib.read_input('input9.txt')
    return list(eval(f'({line})') for line in input)



if __name__ == '__main__':
    run()