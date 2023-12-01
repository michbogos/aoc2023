import re
res = 0

ns = ["one","two","three","four","five","six","seven","eight","nine"]
ps = [re.compile(i) for i in ns]

with open("01.txt", "r") as f:
    for l in f:
        items = []
        for rex in ps:
            rs = rex.finditer(l)
            for e in rs:
                items.append([ns.index(e.group(0))+1, e.start(0)])
        for i in range(len(l)):
            if l[i] in '0123456789':
                items.append((int(l[i]), i))
        items.sort(key=lambda x:x[1])
        res += int(str(items[0][0])+str(items[-1][0]))
print(res)