res = []
with open("04.txt", "r") as f:
    for line in f:
        subtotal = 0
        line = line.split(":")[1]
        winning, owned = line.split("|")
        print(winning, owned)
        owned = [int(i) for i in list(filter(len, owned.split(" ")))]
        winning = [int(i) for i in list(filter(len, winning.split(" ")))]
        for element in owned:
            if element in winning:
                subtotal += 1
        
        if subtotal == 1:
            res.append(subtotal)
        elif subtotal != 0:
            res.append(2**(subtotal-1))

print(sum(res))