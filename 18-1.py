from shapely import geometry

points = []

with open("18-test.txt", "r") as f:
    p = [0, 0]
    points.append(p)
    for line in f:
        d, n, c = line.split(" ")
        n = int(n)
        if d == "R":
            p = (p[0]+n, p[1])
            points.append((p[0]+n, p[1]))
        if d == "L":
            p = (p[0]-n, p[1])
            points.append((p[0]-n, p[1]))
        if d == "D":
            p = (p[0], p[1]+n)
            points.append((p[0], p[1]+n))
        if d == "U":
            p = (p[0], p[1]-n)
            points.append((p[0], p[1]-n))
    
    poly = geometry.Polygon(points)
    print(poly.length)
