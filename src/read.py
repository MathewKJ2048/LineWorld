from geometry import *

import math


def get_lines():
    points_a = list()
    points_b = list()
    R = 10
    r = 2
    theta = 360
    phi = 360
    n = 20
    m = 10
    for i in range(n+1):
        u = math.radians(i / n * theta)
        points_a.append([])
        for j in range(m+1):
            v = math.radians(j/m * phi)
            R_ = R+r*math.sin(v)
            points_a[i].append(Point(R_*math.cos(u),R_*math.sin(u),r*math.cos(v)))

    for j in range(m+1):
        v = math.radians(j/m*phi)
        R_ = R+r*math.sin(v)
        points_b.append([])
        for i in range(n + 1):
            u = math.radians(i / n * theta)
            points_b[j].append(Point(R_*math.cos(u),R_*math.sin(u),r*math.cos(v)))

    return double_dimension(points_b)+double_dimension(points_a)


def single_dimension(points):
    lines = list()
    for i in range(len(points) - 1):
        lines.append((points[i], points[i + 1]))
    return lines


def double_dimension(points):
    lines = list()
    for i in range(len(points)):
        lines += single_dimension(points[i])
    return lines
