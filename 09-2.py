ress = 0

with open("09.txt", 'r') as f:
    for line in f:
        nums = list(reversed([int(i) for i in line.split(" ")]))
        arrays = [nums]
        run = True
        while run:
            arrays.append([])
            for i in range(len(arrays[-2])-1):
                arrays[-1].append(arrays[-2][i+1]-arrays[-2][i])
            if len(set(arrays[-1])) == 1 and arrays[-1][-1]==0:
                run = False
                arrays[-1].append(0)
                for i in range(2, len(arrays)+1):
                    arrays[-i].append(arrays[-i][-1]+arrays[-(i-1)][-1])
        ress += arrays[0][-1]
print(ress)