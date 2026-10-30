# Written with AI
"""
In this file write a program with all necessary clasess functions and methods that accepts list of two-elements tuples with integers - vertices of polygon in coordinate system. Then code should compute smallest rectangle in which polycon can be contained. Sides of rectangle should be parallel to coordinate axes. Then code should compute area of polygon by using Monte-carol method. Points should be randomly chosen inside rectangle. for each [pint code should check whether it is inside polygon. Finally area of polygon should be computed as fraction of rectangle area. Fraction should be equal to the number of points inside polygon divided by total number of randomized points. Main method that computes area shoud accpet parameter two-elements tuples with integers - vertices of polygon in coordinate system and number of random points to be used for calculations
"""
from typing import Sequence, Tuple
import helpers

Point = Tuple[int, int]


class Polygon:
    def __init__(self, vertices: Sequence[Point]) -> None:
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least three vertices.")

        for vertex in vertices:
            if (
                not isinstance(vertex, tuple)
                or len(vertex) != 2
                or type(vertex[0]) is not int
                or type(vertex[1]) is not int
            ):
                raise ValueError("Each vertex must be a tuple of two integers.")

        self.vertices = tuple(vertices)
        min_x, max_x, min_y, max_y = helpers.bounds(self.vertices)
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y

    def contains_point(self, point: Tuple[float, float]) -> bool:
        x, y = point
        inside = False

        for index, (x1, y1) in enumerate(self.vertices):
            x2, y2 = self.vertices[(index + 1) % len(self.vertices)]

            cross_product = (x - x1) * (y2 - y1) - (y - y1) * (x2 - x1)
            if (
                cross_product == 0
                and min(x1, x2) <= x <= max(x1, x2)
                and min(y1, y2) <= y <= max(y1, y2)
            ):
                return True

            if (y1 > y) != (y2 > y):
                intersection_x = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                if x < intersection_x:
                    inside = not inside

        return inside

    def estimate_area(self, number_of_points: int) -> float:
        if type(number_of_points) is not int or number_of_points <= 0:
            raise ValueError("The number of random points must be a positive integer.")

        rectangle_area = helpers.rectangle_area((self.min_x, self.min_y), (self.max_x, self.max_y))
        if rectangle_area == 0:
            return 0.0

        points_inside = 0
        for _ in range(number_of_points):
            point = helpers.random_point((self.min_x, self.min_y), (self.max_x, self.max_y))
            if self.contains_point(point):
                points_inside += 1

        return rectangle_area * points_inside / number_of_points


def estimate_polygon_area(vertices: Sequence[Point], number_of_points: int) -> float:
    """Estimate a polygon's area using uniformly sampled points in its bounding box."""
    return Polygon(vertices).estimate_area(number_of_points)


if __name__ == "__main__":
    example_polygon = [(0, 0), (6, 0), (6, 4), (0, 4)]
    area = estimate_polygon_area(example_polygon, 10_000)
    print(f"Estimated polygon area: {area}")
