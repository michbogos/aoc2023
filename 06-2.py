import tqdm

with open("06.txt", "r") as f:
    lines = f.readlines()
    time = int("".join(list(filter(len, lines[0].replace("Time:", "").split(" ")))))
    distance = int("".join(list(filter(len, lines[1].replace("Distance:", "").split(" ")))))

    res = 0
    print(time)
    print(distance)
    for i in tqdm.trange(0, time+1):
        if i*(time-i) > distance:
            res += 1
    print(res)
