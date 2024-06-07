import random
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def super_triangle(points):
    min_x = min(point.x for point in points)
    min_y = min(point.y for point in points)
    max_x = max(point.x for point in points)
    max_y = max(point.y for point in points)

    dx = max_x - min_x
    dy = max_y - min_y
    delta_max = max(dx, dy)
    mid_x = (min_x + max_x) / 2
    mid_y = (min_y + max_y) / 2

    p1 = Point(mid_x - 20 * delta_max, mid_y - delta_max)
    p2 = Point(mid_x, mid_y + 20 * delta_max)
    p3 = Point(mid_x + 20 * delta_max, mid_y - delta_max)
    return [p1, p2, p3]

def circumcircle(triangle):
    ax, ay = triangle[0].x, triangle[0].y
    bx, by = triangle[1].x, triangle[1].y
    cx, cy = triangle[2].x, triangle[2].y

    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if d == 0:
        return (Point(0, 0), float('inf'))

    ux = ((ax ** 2 + ay ** 2) * (by - cy) + (bx ** 2 + by ** 2) * (cy - ay) + (cx ** 2 + cy ** 2) * (ay - by)) / d
    uy = ((ax ** 2 + ay ** 2) * (cx - bx) + (bx ** 2 + by ** 2) * (ax - cx) + (cx ** 2 + cy ** 2) * (bx - ax)) / d

    center = Point(ux, uy)
    radius = ((center.x - ax) ** 2 + (center.y - ay) ** 2) ** 0.5
    return (center, radius)

def point_in_circumcircle(point, circumcircle):
    center, radius = circumcircle
    distance = ((point.x - center.x) ** 2 + (point.y - center.y) ** 2) ** 0.5
    return distance <= radius

def delaunay_triangulation(points):
    points = points.copy()
    random.shuffle(points)

    super_tri = super_triangle(points)
    triangulation = [[super_tri[0], super_tri[1], super_tri[2]]]

    for point in points:
        bad_triangles = []
        polygon = []

        for triangle in triangulation:
            circum = circumcircle(triangle)
            if point_in_circumcircle(point, circum):
                bad_triangles.append(triangle)
                for i in range(3):
                    edge = (triangle[i], triangle[(i + 1) % 3])
                    if edge not in polygon and edge[::-1] not in polygon:
                        polygon.append(edge)
                    elif edge in polygon:
                        polygon.remove(edge)
                    elif edge[::-1] in polygon:
                        polygon.remove(edge[::-1])

        for triangle in bad_triangles:
            triangulation.remove(triangle)

        for edge in polygon:
            new_tri = [edge[0], edge[1], point]
            triangulation.append(new_tri)

    triangulation = [tri for tri in triangulation if not any(p in super_tri for p in tri)]
    return triangulation

def plot_triangulation(triangulation, points):
    for triangle in triangulation:
        t = plt.Polygon([[p.x, p.y] for p in triangle], edgecolor='black', fill=None)
        plt.gca().add_patch(t)

    for point in points:
        plt.plot(point.x, point.y, 'o')

    plt.show()

# Example usage
points = [Point(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(20)]
triangulation = delaunay_triangulation(points)
plot_triangulation(triangulation, points)
