"""
OOP Classes to Handle 2D Coordinate Scenarios

This module supports:
- Creating and displaying 2D coordinates
- Finding the distance between two points
- Calculating distance from origin
- Checking if a point lies on a given line
- Finding the shortest distance from a point to a line
"""

class Point:
    """
    Represents a 2D point with x and y coordinates.
    """

    def __init__(self, x, y):
        """
        Initializes a point at the given x and y coordinates.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the point.
        """
        return f"<{self.x}, {self.y}>"

    def euclidean_distance(self, other):
        """
        Calculates and returns the Euclidean distance between two points.
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def distance_from_origin(self):
        """
        Returns the distance of the point from the origin (0,0).
        """
        return self.euclidean_distance(Point(0, 0))


class Line:
    """
    Represents a line in 2D space defined by the equation Ax + By + C = 0.
    """

    def __init__(self, A, B, C):
        """
        Initializes the line using its coefficients A, B, and C.
        """
        self.A = A
        self.B = B
        self.C = C

    def __str__(self):
        """
        Returns a readable form of the line equation.
        """
        return f"{self.A}x + {self.B}y + {self.C} = 0"

    def point_on_line(self, point):
        """
        Checks whether a given point lies on this line.
        """
        result = self.A * point.x + self.B * point.y + self.C
        if result == 0:
            return "Lies on the Line"
        else:
            return "Doesn't lie on the Line"

    def shortest_distance(self, point):
        """
        Calculates the shortest (perpendicular) distance from a point to the line.
        """
        numerator = abs(self.A * point.x + self.B * point.y + self.C)
        denominator = (self.A ** 2 + self.B ** 2) ** 0.5
        return numerator / denominator


# ----------- Usage -----------

p1 = Point(10, 10)
p2 = Point(1, 1)

# Distance between two points
print(p1.euclidean_distance(p2))

# Distance from origin
print(p1.distance_from_origin())

# Define a line: x + y - 2 = 0
l1 = Line(1, 1, -2)

print(l1)
print(p2)

# Check if p2 lies on the line
print(l1.point_on_line(p2))

# Shortest distance from p2 to the line
print(l1.shortest_distance(p2))
