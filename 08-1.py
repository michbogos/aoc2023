nodes = {}
instrucations = ""
instruction = 0
current = "AAA"
with open("08.txt", "r") as f:
    for line in f:
        if line.count("="):
            line = line.replace("=", "")
            line = line.replace("(", "")
            line = line.replace(")", "")
            line = line.replace(",", "")
            start, l, r = [i.replace("\n", "") for i in list(filter(len, line.split(" ")))]
            nodes[start] = (l, r)
        else:
            instructions = line.replace("\n", "")
    while current != "ZZZ":
        if instructions[instruction%len(instructions)] == "L":
            current = nodes[current][0]
        elif instructions[instruction%len(instructions)] == "R":
            current = nodes[current][1]
        instruction += 1
    
    print(instruction)
