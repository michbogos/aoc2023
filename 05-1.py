intervals = []

with open("05.txt", "r") as f:
    seeds = []
    data = []
    for line in f:
        if line.find("seeds:") != -1:
            seeds = [int(i) for i in line.split(" ")[1:]]
            print(seeds)
        if ':' in line and len(line) > 1:
            data.append([])
        elif len(line) > 1:
            data[-1].append([int(i) for i in line.split()])
            data[-1] = list(filter(len, data[-1]))
    
    to_check = []

    data = filter(len, data)

    for dim in data:
        for i, seed in enumerate(seeds):
            for interval in dim:
                if seed >= interval[1] and seed <= interval[1]+interval[2]:
                    seeds[i] = interval[0] + (seed-interval[1])
    
    print(min(seeds))