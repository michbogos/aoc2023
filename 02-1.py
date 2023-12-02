import re
import time

r=12
g=13
b=14

res = 0

with open("02.txt", "r") as f:
    for j, line in enumerate(f):
        line = line.split(":")[1].replace("\n", "")
        games = line.split(";")
        possible = True
        for i, game in enumerate(games):
            turns = list(filter(len, game.split(" ")))
            turns = [turn.replace(",", "") for turn in turns]
            try:
                idx = turns.index("red")
                ra = int(turns[idx-1])
                if ra > r:
                    possible = False
                    break
            except ValueError:
                ra = 0
            try:
                idx = turns.index("green")
                ga = int(turns[idx-1])
                if ga > g:
                    possible = False
                    break
            except:
                ga = 0
            try:
                idx = turns.index("blue")
                ba = int(turns[idx-1])
                if ba > b:
                    possible = False
                    break
            except:
                ba = 0
        if possible:
            res += j+1
    print(res)