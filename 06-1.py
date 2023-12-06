with open("06-test.txt", "r") as f:
    lines = f.readlines()
    times = [int(i) for i in filter(len, lines[0].replace("Time:", "").split(" "))]
    distances = [int(i) for i in filter(len, lines[1].replace("Distance:", "").split(" "))]

    ress = 1

    for time, distance in zip(times, distances):
        res = 0
        for i in range(0, time+1):
            if i*(time-i) > distance:
                res += 1
        ress*= res
    print(ress)
