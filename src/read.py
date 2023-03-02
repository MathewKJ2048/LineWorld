import json

from geometry import Point


def read():  # returns a list of tuples of points
    figure = open("mesh.json", "r").read()
    structures = json.loads(figure)["structures"]
    lines = list()
    for s in structures:
        content = s["content"]
        if s["type"] == "line":
            lines += get_line(content)
        elif s["type"] == "curve:":
            lines += get_curve(content)
        elif s["type"] == "surface":
            lines += get_surface(content)
    return lines


def get_point(p):
    return Point(p["x"], p["y"], p["z"])


def get_line(line):
    p1 = get_point(line[0])
    p2 = get_point(line[1])
    return list().append((p1, p2))


def get_curve(curve):
    points = list()
    for c in curve:
        points.append(get_point(c))
    return single_dimension(points)


def get_surface(surface):
    points = list()
    for s in surface:
        p = list()
        for t in s:
            p.append(get_point(t))
        points.append(p)
    return double_dimension(points)


def single_dimension(points):
    lines = list()
    for i in range(len(points) - 1):
        lines.append((points[i], points[i + 1]))
    return lines


def double_dimension(points):
    lines = list()
    for i in range(len(points)):
        lines += single_dimension(points[i])
    for j in range(len(points[0])):
        cross_points = []
        for i in range(len(points)):
            cross_points.append(points[i][j])
        lines += single_dimension(cross_points)
    return lines
