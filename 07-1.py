from functools import cmp_to_key

values = {element:i+1 for i, element in enumerate("23456789TJQKA")}

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

def compare(ela, elb):
    a = ela[0]
    b = elb[0]
    typea = getType(a)
    typeb = getType(b)
    if typea > typeb:
        return 1
    if typea < typeb:
        return -1
    else:
        for x, y in zip(a, b):
            if values[x] > values[y]:
                return 1
            elif values[x] < values[y]:
                return -1
        return 0


with open("07.txt", "r") as f:
    hands = {}
    for line in f:
        hand, value = line.split(" ")
        hands[hand] = int(value.replace("\n", ""))
    
    ranks = sorted(hands.items(), key=cmp_to_key(compare))
    res = 0
    for i, el in enumerate(ranks):
        res += (i+1)*el[1]
    
    print(res)