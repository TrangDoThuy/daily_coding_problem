"""
This problem was asked by Nvidia.

You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon. 
You can assume these points are given in order; 
that is, you can construct the polygon by connecting point 1 to point 2, point 2 to point 3, and so on, 
finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, you should return False).

Ray casting algorithm:
One simple way of finding whether the point is inside or outside a simple polygon is to test how many times a ray, 
starting from the point and going in any fixed direction, intersects the edges of the polygon. 
If the point is on the outside of the polygon the ray will intersect its edge an even number of times. 
If the point is on the inside of the polygon then it will intersect the edge an odd number of times. 

FYI:

https://www.geeksforgeeks.org/cses-solutions-point-in-polygon/

https://en.wikipedia.org/wiki/Sweep_line_algorithm#:~:text=In%20computational%20geometry%2C%20a%20sweep,critical%20techniques%20in%20computational%20geometry.

"""

import unittest

def is_on_segment(segment, point):
    x1, y1 = segment[0]
    x2, y2 = segment[1]
    x, y = point

    u_x = x - x1
    u_y = y - y1

    v_x = x - x2
    v_y = y - y2

    is_within_bounds = (min(x1, x2) <= x <= max(x1, x2)) and \
                       (min(y1, y2) <= y <= max(y1, y2))
                       
    is_collinear = (u_x*v_y == u_y*v_x)
    
    return is_within_bounds and is_collinear

def is_in_polygon(polygon_points, new_point):
    x, y = new_point
    count = 0
    n = len(polygon_points)
    for i in range(n):
        a = polygon_points[i]
        b = polygon_points[(i+1) % n]

        if is_on_segment([a, b], new_point):
            return False

        #keep x, y increase into inf
        if a[0] > b[0]:
            a, b = b, a
        if a[0] <= x < b[0]:
            y_intersect = (b[1] - a[1]) * (x - a[0]) / (b[0] - a[0]) + a[1]
            if y < y_intersect:
                count += 1

    return count % 2 != 0

class TestPointInPolygon(unittest.TestCase):
    def test_0(self):
        polygon_points= [(0, 0), (4, 0), (4, 4), (0, 4)]
        new_point = (2, 2)
        self.assertTrue(is_in_polygon(polygon_points, new_point))
        return

    def test_1(self):
        polygon_points= [(0, 0), (4, 0), (4, 4), (0, 4)]
        new_point = (1, 1)
        self.assertTrue(is_in_polygon(polygon_points, new_point))
        return
    def test_2(self):
        polygon_points= [(0, 0), (4, 0), (4, 4), (0, 4)]
        new_point = (5, 3)
        self.assertFalse(is_in_polygon(polygon_points, new_point))
        return
    def test_3(self):
        polygon_points= [(0, 0), (4, 0), (4, 4), (0, 4)]
        new_point = (0, 4)
        self.assertFalse(is_in_polygon(polygon_points, new_point))
        return
unittest.main()