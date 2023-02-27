import math


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def print(self):
        print("(" + str(int(self.x)) + "," + str(int(self.y)) + "," + str(int(self.z)) + ")")


class Vector:
    # ai + bj + ck
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def modulus(self):
        return math.sqrt(self.a ** 2 + self.b ** 2 + self.c ** 2)


class Plane(Vector):
    # ax+by+cz=d
    def __init__(self, vector, point):
        super().__init__(vector.a, vector.b, vector.c)
        self.d = self.a * point.x + self.b * point.y + self.c * point.z


class Line(Vector):
    # (x-p.x)/a = (y-p.y)/b = (z-p.z)/c
    def __init__(self, vector, point):
        super().__init__(vector.a, vector.b, vector.c)
        self.point = point


def distance_point_point(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2 + (point1.z - point2.z) ** 2)


def distance_point_from_line(point, line):
    v = vector_from_two_points(point, line.point)
    return cross(line, v).modulus() / line.modulus()


def vector_from_two_points(point1, point2):
    return Vector(point2.x - point1.x, point2.y - point1.y, point2.z - point1.z)


def line_from_two_points(point1, point2):
    return Line(vector_from_two_points(point1, point2), point1)


def line_cut_plane_at(line, plane):
    A = plane.a
    B = plane.b
    C = plane.c
    D = plane.d
    a = line.a
    b = line.b
    c = line.c
    x1 = line.point.x
    y1 = line.point.y
    z1 = line.point.z
    H = A * a + B * b + C * c
    if H == 0:
        H = 0.00000001
    t = (D - (A * x1 + B * y1 + C * z1)) / H
    return Point(a * t + x1, b * t + y1, c * t + z1)


def is_ordered(p1, p2, p3):
    Dx = (p1.x - p2.x) * (p3.x - p2.x)
    Dy = (p1.y - p2.y) * (p3.y - p2.y)
    Dz = (p1.z - p2.z) * (p3.z - p2.z)
    return Dx <= 0 and Dy <= 0 and Dz <= 0


def cross(v1, v2):
    return Vector(v1.b * v2.c - v1.c * v2.b,
                  v1.c * v2.a - v1.a * v2.c,
                  v1.a * v2.b - v2.a * v1.b)


def dot(v1, v2):
    return v1.a * v2.a + v1.b * v2.b + v1.c * v2.c
