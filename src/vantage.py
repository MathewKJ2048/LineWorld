import math

import geometry
from geometry import *


class Vantage(Point):
    def __init__(self, screen_distance, screen_width, screen_height):
        super().__init__(-30, 0, 0)
        self.screen_distance = screen_distance
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.v_x = 0
        self.v_y = 0
        self.v_z = 0
        self.theta = 0  # polar angle
        self.phi = 90  # azimuthal angle
        self.w_theta = 0
        self.w_phi = 0
        self.window_centre_cache = None
        self.window_vector_cache = None
        self.window_plane_cache = None

    def step(self, dt):
        self.x += dt * self.v_x
        self.y += dt * self.v_y
        self.z += dt * self.v_z
        self.theta += dt * self.w_theta
        self.phi += dt * self.w_phi
        if self.phi <= 0:
            self.phi = 1
        if self.phi >= 180:
            self.phi = 179
        self.window_centre_cache = None
        self.window_vector_cache = None
        self.window_plane_cache = None

    def window_centre(self):
        if self.window_centre_cache is not None:
            return self.window_centre_cache
        return Point(
            self.x + self.screen_distance * math.cos(math.radians(self.theta)) * math.sin(math.radians(self.phi)),
            self.y + self.screen_distance * math.sin(math.radians(self.theta)) * math.sin(math.radians(self.phi)),
            self.z + self.screen_distance * math.cos(math.radians(self.phi))
        )

    def window_vector(self):
        if self.window_vector_cache is not None:
            return self.window_vector_cache
        return vector_from_two_points(self, self.window_centre())

    def window_plane(self):
        if self.window_plane_cache is not None:
            return self.window_plane_cache
        return Plane(self.window_vector(), self.window_centre())

    def project(self, point):
        l = line_from_two_points(self, point)
        p_ = line_cut_plane_at(l, self.window_plane())
        if is_ordered(self, p_, point):
            return p_
        return None

    def window_vertical(self):
        p = Point(
            self.x + self.screen_distance * math.cos(math.radians(self.theta)) * math.sin(math.radians(self.phi + 1)),
            self.y + self.screen_distance * math.sin(math.radians(self.theta)) * math.sin(math.radians(self.phi + 1)),
            self.z + self.screen_distance * math.cos(math.radians(self.phi + 1))
        )
        L = line_from_two_points(self, p)
        p_ = line_cut_plane_at(L, self.window_plane())
        return line_from_two_points(self.window_centre(), p_)

    def window_horizontal(self):
        p = Point(
            self.x + self.screen_distance * math.cos(math.radians(self.theta + 1)) * math.sin(math.radians(self.phi)),
            self.y + self.screen_distance * math.sin(math.radians(self.theta + 1)) * math.sin(math.radians(self.phi)),
            self.z + self.screen_distance * math.cos(math.radians(self.phi))
        )
        L = line_from_two_points(self, p)
        p_ = line_cut_plane_at(L, self.window_plane())
        return line_from_two_points(self.window_centre(), p_)

    def get_x_y(self, point_projected):
        x_ = distance_point_from_line(point_projected, self.window_vertical())
        y_ = distance_point_from_line(point_projected, self.window_horizontal())
        D = cross(self.window_vector(), vector_from_two_points(self.window_centre(), point_projected))
        D_x = -1 if D.c >= 0 else 1
        D_y = -1 if cross(self.window_vector(), D).c >= 0 else 1

        return (self.screen_width / 2) + D_x * x_, self.screen_height / 2 + D_y * y_
