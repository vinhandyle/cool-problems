# Day 22: Monkey Market
# Part 1: 18694566361
# Part 2: 2100

import lib

def run():
    arr = process_input()  

    # Calculate and save secret nums
    sdict, tot = dict(), 0
    for n in arr:
        tot += secret_num(n, 2000, sdict)
    print(tot)

    # Get price and price change per day for each buyer
    prices, deltas = [], []
    for s in sdict.values():
        prices.append(get_price(s))
    for p in prices:
        deltas.append(get_delta(p))

    # Get first price of each chain per buyer, 
    # then group collectively by chain
    cdict = dict()
    for i in range(len(deltas)):
        get_chains(prices[i], deltas[i], cdict)
        
    mx = (0,0)
    for c in cdict:
        if sum(cdict[c]) > mx[0]:
            mx = (sum(cdict[c]), c)
    print(mx)



def merge_chains(chains):
    merge = set()
    for c in chains:
        for v in c.values():
            merge = merge.union(v)
    return merge



def get_chains(prices, deltas, cdict):
    chains = set()
    for i in range(4, len(prices)):
        c = (deltas[i-3], deltas[i-2], deltas[i-1], deltas[i])
        if c not in chains:
            chains.add(c)
            if c not in cdict:
                cdict[c] = []
            cdict[c].append(prices[i])
        


def get_delta(prices):
    arr = [0]
    for i in range(1, len(prices)):
        arr.append(prices[i] - prices[i-1])
    return arr



def get_price(seq):
    arr = []
    for n in seq:
        arr.append(n % 10)
    return arr



def secret_num(n, i, sdict):
    s = n
    sdict[n] = [n]
    for j in range(i):
        s = prune(mix(s, s * 64))
        s = prune(mix(s, s // 32))
        s = prune(mix(s, s * 2048))
        sdict[n].append(s)
    return s



def mix(a, b):
    return a ^ b

assert mix(42, 15) == 37



def prune(a):
    return a % 16777216

assert prune(100000000) == 16113920



def process_input():
    return list(int(line) for line in lib.read_input('input22.txt'))



if __name__ == '__main__':
    run()