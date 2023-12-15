def HASH(x):
    res = 0
    for char in x:
        res += ord(char)
        res *= 17
        res %= 256
    return res

with open("15.txt", "r") as f:
    print(sum([HASH(item.replace("\n", "")) for item in f.readline().split(",")]))