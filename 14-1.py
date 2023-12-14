import tqdm
import functools


s = []

def move(mat):
    for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == "O":
                    dy = 0
                    while i+dy-1 > -1 and mat[i+dy-1][j]==".":
                        dy-=1
                    mat[i][j] = "."
                    mat[i+dy][j] = "O"
    #West
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == "O":
                dx = 0
                while j+dx-1 > -1 and mat[i][j+dx-1]==".":
                    dx-=1
                mat[i][j] = "."
                mat[i][j+dx] = "O"
    #South
    for i in range(len(mat)-1, -1, -1):
        for j in range(len(mat[i])):
            if mat[i][j] == "O":
                dy = 0
                while i+dy+1 < len(mat) and mat[i+dy+1][j]==".":
                    dy+=1
                mat[i][j] = "."
                mat[i+dy][j] = "O"
    #East
    for i in range(len(mat)):
        for j in range(len(mat[i])-1, -1, -1):
            if mat[i][j] == "O":
                dx = 0
                while j+dx+1 < len(mat[0]) and mat[i][j+dx+1]==".":
                    dx+=1
                mat[i][j] = "."
                mat[i][j+dx] = "O"
    
    return mat
    


with open("14.txt", "r") as f:
    mat = tuple([[char for char in line if char != "\n"] for line in f])
    s.append(mat)
    for cycle in range(0, 1000000000):
        mat = move(mat)
        if mat in s:
            print(cycle)
            print(mat)
            break
        s.append(mat)
    res = 0
    mat = s[1000000000%len(s)]
    for i in range(len(mat)):
        for char in mat[i]:
            if char == "O":
                res += len(mat)-i
    print(res)
