r=12
g=13
b=14

res = 0
power = 0

with open("02.txt", "r") as f:
    for j, line in enumerate(f):
        line = line.split(":")[1].replace("\n", "")
        games = line.split(";")
        possible = True
        minr, ming, minb = (-10e10, -10e10, -10e10)
        for i, game in enumerate(games):
            turns = list(filter(len, game.split(" ")))
            turns = [turn.replace(",", "") for turn in turns]
            try:
                idx = turns.index("red")
                ra = int(turns[idx-1])
                if ra > r:
                    possible = False
            except ValueError:
                ra = 0
            minr = max(minr, ra)
            try:
                idx = turns.index("green")
                ga = int(turns[idx-1])
                if ga > g:
                    possible = False
            except:
                ga = 0
            ming = max(ming, ga)
            try:
                idx = turns.index("blue")
                ba = int(turns[idx-1])
                if ba > b:
                    possible = False
            except:
                ba = 0
            minb = max(minb, ba)
        if possible:
            res += j+1
        power += minr*minb*ming 
    print(f"Res: {res}")
    print(f"Power: {power}")