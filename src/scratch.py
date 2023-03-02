from write import *
import math
from geometry import Point

points = list()

R = 20
r = 5
theta = 360
phi = 360
n = 20
m = 10
for i in range(n + 1):
    u = math.radians(i / n * theta)
    points.append([])
    for j in range(m + 1):
        v = math.radians(j / m * phi)
        R_ = R + r * math.sin(v)
        points[i].append(Point(R_ * math.cos(u), R_ * math.sin(u), r * math.cos(v)))

add_surface(points)
write()
