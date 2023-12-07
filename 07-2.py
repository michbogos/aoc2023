from functools import cmp_to_key
import re
import math

values = {element:i+1 for i, element in enumerate("J23456789TQKA")}

cards = "J23456789TQKA"

def permute(x, v):
    best = x
    bestValue = 0
    indices = [element.start(0) for element in re.finditer("J", x)]
    if len(indices) == 0:
        return (x, getType(x), x, v)
    repl = [0 for i in range(len(indices))]
    for _ in range(len(cards)**len(indices)-1):
        repl[0]+=1
        for i in range(1, len(indices)):
            if repl[i-1] == len(cards):
                repl[i-1] = 0
                repl[i] += 1
        
        replaced = [i for i in x]
        for i, index in enumerate(indices):
            replaced[index] = cards[repl[i]]
            value = getType("".join(replaced))
            if value > bestValue:
                bestValue = value
                best = "".join(replaced)
    
    return (best, bestValue, x, v)

def getType(x:str):
    s = set(x)
    # Five of a kind
    if len(s) == 1:
        return 8
    # Four of a kind
    if len(s) == 2:
        for element in s:
            if x.count(element) == 4:
                return 7
    # Full house
    if len(s) == 2:
        res = 0
        for element in s:
            res = max(res, x.count(element))
        if res == 3:
            return 6
    # Three of a kind
    if len(s) == 3:
        res = 0
        for element in s:
            res = max(res, x.count(element))
        if res == 3:
            return 5
    # Two pair
    if len(s) == 3:
        res = 0
        for element in s:
            res = max(res, x.count(element))
        if res == 2:
            return 4
    
    # One pair
    if len(s) == 4:
        return 3
    
    # High Card
    if len(s) == 5:
        return 2
    
    return 1

def compare(a, b):
    if a[1] > b[1]:
        return 1
    if a[1] < b[1]:
        return -1
    else:
        for x, y in zip(a[2], b[2]):
            if values[x] > values[y]:
                return 1
            elif values[x] < values[y]:
                return -1
        return 0


with open("07.txt", "r") as f:
    hands = {}
    arr = []
    for line in f:
        hand, value = line.split(" ")
        hands[hand] = int(value.replace("\n", ""))
        arr.append(permute(hand, int(value)))

    
    ranks = sorted(arr, key=cmp_to_key(compare))
    res = 0
    for i, el in enumerate(ranks):
        res += (i+1)*el[-1]
    
    print(ranks)
    print(res)