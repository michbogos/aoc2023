import math
nodes = {}
instrucations = ""
instruction = 0
currents = []
loops = []
run = True


def run():
    for pos in currents:
        if not pos.endswith("Z"):
            return True
    return False
with open("08.txt", "r") as f:
    for line in f:
        if line == "\n":
            continue
        if line.count("="):
            line = line.replace("=", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace(",", "")
            start, l, r = [i.replace("\n", "") for i in list(filter(len, line.split(" ")))]
            if start.endswith("A"):
                currents.append(start)
            nodes[start] = (l, r)
        else:
            instructions = line.replace("\n", "")

    for i, node in enumerate(currents):
        current = node
        instruction = 0
        while not current.endswith("Z"):
            if instructions[instruction%len(instructions)] == "L":
                current = nodes[current][0]
            elif instructions[instruction%len(instructions)] == "R":
                current = nodes[current][1]
            instruction += 1
        loops.append(instruction)
    print(loops)

    print(math.lcm(*loops))