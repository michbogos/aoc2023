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


    data = filter(len, data)

    seeds = [(seeds[2*i]. seeds[2*i+1]) for i in range(seeds/2)]

    for dim in data:
        ranges = []
        for i, seed in enumerate(seeds):
            start, length = seed
            for interval in dim:
                if start+length < interval[1]:
                    ranges.append([start, length])
                elif start < interval[1] and (start+length > interval[1] and start+length <= interval[1]+interval[2]):
                    ranges.append([start, interval[1]-1])
                    ranges.append([interval[0], interval[0]+(start+length-interval[1])])
                elif (start >= interval[1] and start <= interval[1]) and (start+length >= interval[1] and start+length <= interval[1]+interval[2]):
                    ranges.append([interval, interval[0]+length])
    
    print(min(seeds))