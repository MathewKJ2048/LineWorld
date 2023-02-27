from geometry import *

def get_lines():
    lines = list()
    lines.append((Point(0,0,0), Point(0,0,10)))
    lines.append((Point(0,0,10), Point(0,10,10)))
    lines.append((Point(0,10,0), Point(0,10,10)))
    lines.append((Point(0,0,0), Point(0,10,0)))
    lines.append((Point(0,0,0), Point(0,10,0)))
    lines.append((Point(0,0,0), Point(10,0,0)))
    lines.append((Point(10,10,0), Point(0,10,0)))
    lines.append((Point(10,10,0), Point(10,0,0)))
    lines.append((Point(0,0,0), Point(0,0,10)))
    lines.append((Point(0,0,0), Point(10,0,0)))
    lines.append((Point(10,0,10), Point(10,0,0)))
    lines.append((Point(10,0,10), Point(0,0,10)))
    return lines