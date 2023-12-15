boxes = [[] for _ in range(256)]
label_lens = {}


def HASH(x):
    res = 0
    for char in x:
        res += ord(char)
        res *= 17
        res %= 256
    return res

with open("15.txt", "r") as f:
    instructions = [item.replace("\n", "") for item in f.readline().split(",")]
    for instruction in instructions:
        if "-" in instruction:
            label = instruction.replace("-", "")
            h = HASH(label)
            try:
                del boxes[h][boxes[h].index(label)]
            except ValueError:
                print("Not found")
        if "=" in instruction:
            label, lens = instruction.split("=")
            h = HASH(label)
            label_lens[label] = lens
            if label not in boxes[h]:
                boxes[h].append(label)
    res = 0
    for i, box in enumerate(boxes):
        for j, label in enumerate(box):
            res += (i+1)*(j+1)*int(label_lens[label])
    
    print(res)