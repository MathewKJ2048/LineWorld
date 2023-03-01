import pygame
import time
import json
from vantage import *
import os
import read

pygame.init()
f = open("config.json", "r")
config_raw = f.read()
config = json.loads(config_raw)
screen = pygame.display.set_mode((config["width"], config["height"]))

c = pygame.time.Clock()
V = Vantage(config["screen_distance"], config["width"] / config["scale"], config["height"] / config["scale"])


def process_input():
    global V
    global config
    v_m = config["velocity"]
    w_phi_m = config["polar_velocity"]
    w_theta_m = config["azimuthal_velocity"]
    v_x = 0
    v_y = 0
    v_z = 0
    w_phi = 0
    w_theta = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_j]:
        w_theta += w_theta_m
    if keys[pygame.K_l]:
        w_theta -= w_theta_m
    if keys[pygame.K_i]:
        w_phi -= w_phi_m
    if keys[pygame.K_k]:
        w_phi += w_phi_m
    if keys[pygame.K_w]:
        v_x += v_m
    if keys[pygame.K_x]:
        v_x -= v_m
    if keys[pygame.K_a]:
        v_y += v_m
    if keys[pygame.K_d]:
        v_y -= v_m
    if keys[pygame.K_e]:
        v_z -= v_m
    if keys[pygame.K_z]:
        v_z += v_m
    if keys[pygame.K_t]:
        v_z += v_m * math.cos(math.radians(V.phi))
        v_x += v_m * math.sin(math.radians(V.phi)) * math.cos(math.radians(V.theta))
        v_y += v_m * math.sin(math.radians(V.phi)) * math.sin(math.radians(V.theta))
    if keys[pygame.K_g]:
        v_z -= v_m * math.cos(math.radians(V.phi))
        v_x -= v_m * math.sin(math.radians(V.phi)) * math.cos(math.radians(V.theta))
        v_y -= v_m * math.sin(math.radians(V.phi)) * math.sin(math.radians(V.theta))

    V.v_z = v_z
    V.v_y = v_y
    V.v_x = v_x
    V.w_phi = w_phi
    V.w_theta = w_theta


def render(line):
    global V
    global config
    point1, point2 = line
    p_1 = V.project(point1)
    p_2 = V.project(point2)
    if p_2 is None or p_1 is None:  # case where line cuts through the screen
        p_mid = line_cut_plane_at(line_from_two_points(point1, point2), V.window_plane())
        if is_ordered(point1, p_mid, point2):
            p_ = p_1 if p_2 is None else p_2
            p_1 = p_
            p_2 = p_mid
            if p_ is None:
                return
        else:
            return
    x1, y1 = V.get_x_y(p_1)
    x2, y2 = V.get_x_y(p_2)
    pygame.draw.line(screen, config["foreground"], transform(x1, y1), transform(x2, y2))


def transform(x, y):
    global config
    x_ = x * config["scale"]
    y_ = config["height"] - config["scale"] * y
    return [x_, y_]


lines = read.get_lines()
# lines.append((Point(),Point()))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt = c.tick(config["max_frame_rate"])
    process_input()
    V.step(dt)

    screen.fill(config["background"])
    ti = time.time()
    for line in lines:
        render(line)
    pygame.display.update()
    tf = time.time()
    digits = 3
    rt = round((tf - ti), 3)

    os.system("cls")
    print("position:")
    V.print()
    print("theta: " + str(int(V.theta)) + "\tphi: " + str(int(V.phi)))
    print("render time (ns): " + str(rt))
