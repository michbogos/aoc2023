import sys
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


sys.setrecursionlimit(100000)

mat = []
visited = []
start_pos = []
graph = {}

points = []

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

queue = []


def bfs():
    while len(queue) > 0:
        x,y = queue[0]
        del queue[0]
        if x+1>-1 and x+1 < len(mat[y]):
            if isRightPossible(mat[y][x], mat[y][x+1]) and visited[y][x+1]==0:
                queue.append((x+1, y))
                visited[y][x+1] = visited[x][y]+1

        if x-1>-1 and x-1 < len(mat[y]):
            if isLeftPossible(mat[y][x], mat[y][x-1]) and visited[y][x-1]==0:
                queue.append((x-1, y))
                visited[y][x-1] = visited[x][y]+1

        if y+1>-1 and y+1 < len(mat):
            if isDownPossible(mat[y][x], mat[y+1][x]) and visited[y+1][x]==0:
                queue.append((x,y+1))
                visited[y+1][x] = visited[x][y]+1

        if y-1>-1 and y-1 < len(mat):
            if isUpPossible(mat[y][x], mat[y-1][x]) and visited[y-1][x]==0:
                queue.append((x,y-1))
                visited[y-1][x] = visited[x][y]+1

def dfs(x, y):
    visited[y][x] = True
    points.append((x, y))
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
            queue.append((loc, i))
            start_pos = [loc, i]
    
    dfs(*start_pos)
    res = 0
    for i in visited:
        for j in i:
            if j == True:
                res += 1


    poly = Polygon(points)
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if mat[y][x] == ".":
                p = Point(x+0.5, y+0.5)

    print(visited)
    print(points)
    print(res)
    print(poly.area+1-res/2)