import sys
sys.setrecursionlimit(100000)

mat = []
visited = []
start_pos = []
graph = {}

def isUpPossible(a, b):
    if a in "|LJ" and b in "|F7":
        return True
    else:
        return False

def isDownPossible(a, b):
    if a in "|F7" and b in "|LJ":
        return True
    else:
        return False

def isRightPossible(a, b):
    if a in "-LF" and b in "-J7":
        return True
    else:
        return False

def isLeftPossible(a, b):
    if a in "-J7" and b in "-LF":
        return True
    else:
        return False


def dfs(x, y):
    visited[y][x] = True
    if x+1>-1 and x+1 < len(mat[y]):
            if isRightPossible(mat[y][x], mat[y][x+1]) and visited[y][x+1]==False:
                dfs(x+1, y)

    if x-1>-1 and x-1 < len(mat[y]):
        if isLeftPossible(mat[y][x], mat[y][x-1]) and visited[y][x-1]==False:
            dfs(x-1, y)

    if y+1>-1 and y+1 < len(mat):
        if isDownPossible(mat[y][x], mat[y+1][x]) and visited[y+1][x]==False:
            dfs(x,y+1)

    if y-1>-1 and y-1 < len(mat):
        if isUpPossible(mat[y][x], mat[y-1][x]) and visited[y-1][x]==False:
            dfs(x,y-1)

with open("10.txt", "r") as f:
    for i, line in enumerate(f):
        mat.append(list(filter(lambda x: x!="\n", [char for char in line.replace("S", "F")])))
        visited.append([0 for _ in range(len(mat[-1]))])
        loc = line.find("S")
        if loc > 0:
            start_pos = [loc, i]
    
    dfs(*start_pos)
    res = 0
    for i in visited:
        for j in i:
            if j == True:
                res += 1
    print(res//2)