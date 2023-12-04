res = []
cards = [0 for _ in range(201)]
with open("04.txt", "r") as f:
    for i, line in enumerate(f):
        subtotal = 0
        line = line.split(":")[1]
        winning, owned = line.split("|")
        print(winning, owned)
        owned = [int(i) for i in list(filter(len, owned.split(" ")))]
        winning = [int(i) for i in list(filter(len, winning.split(" ")))]
        for element in owned:
            if element in winning:
                subtotal += 1
        for j in range(i+1, i+subtotal+1):
            cards[j]+=cards[i]+1

print(sum(cards)+201)