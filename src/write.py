import json

# a simple script file to generate various structures
items = {"structures": []}


def get_point(p):
    return {"x": p.x, "y": p.y, "z": p.z}


def add_line(point1, point2):
    d = {"type": "line", "content": [get_point(point1), get_point(point2)]}
    items["structures"].append(d)


def add_curve(points):
    json_points = []
    for p in points:
        json_points.append(get_point(p))
    d = {"type": "curve", "content": json_points}
    items["structures"].append(d)


def add_surface(points):
    json_points = []
    for plist in points:
        json_plist = []
        for p in plist:
            json_plist.append(get_point(p))
        json_points.append(json_plist)
    d = {"type": "surface", "content": json_points}
    items["structures"].append(d)


def write():
    json_object = json.dumps(items, indent=4)
    with open("mesh.json", "w") as outfile:
        outfile.write(json_object)


