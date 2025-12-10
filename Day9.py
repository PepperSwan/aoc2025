with open("input9.txt") as f:
    points = [[int(x) for x in line.strip().split(',')] for line in f]

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

rectangles = {}
for i in range(len(points)):
    for j in range(i+1,len(points)):
        rectangles[(i, j)] = area(points[i], points[j])
rectangles = [[k, v] for k, v in sorted(rectangles.items(), key=lambda item: item[1], reverse=True)]

print("Part 1:", rectangles[0][1])

edges = []
for i in range(len(points)):
    x1, y1 = points[i]
    x2, y2 = points[(i+1) % len(points)]
    edges.append(((x1, y1), (x2, y2)))

def point_inside(p):
    crossings = 0
    for (x1, y1), (x2, y2) in edges:
        if x1 == x2:
            vx = x1
            y_low, y_high = sorted((y1, y2))
            if y_low <= p[1] < y_high and vx > p[0]:
                crossings += 1
    return crossings % 2 == 1

def edge_crosses(x1, y1, x2, y2, xmin, xmax, ymin, ymax):
    if x1 == x2:
        x = x1
        if xmin < x < xmax:
            e_ymin, e_ymax = sorted((y1, y2))
            return not (e_ymax <= ymin or e_ymin >= ymax)
        return False
    else:
        y = y1
        if ymin < y < ymax:
            e_xmin, e_xmax = sorted((x1, x2))
            return not (e_xmax <= xmin or e_xmin >= xmax)
        return False

for r, v in rectangles:
    x1, y1 = points[r[0]]
    x2, y2 = points[r[1]]
    xmin, xmax = sorted((x1, x2))
    ymin, ymax = sorted((y1, y2))

    cx = (xmin + xmax) / 2
    cy = (ymin + ymax) / 2
    if not point_inside((cx, cy)):       
        continue

    for (ex1, ey1), (ex2, ey2) in edges:
        if edge_crosses(ex1, ey1, ex2, ey2, xmin, xmax, ymin, ymax):
            break
    else:
        print("Part 2:", v)
        break