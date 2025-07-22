"""
OOP Classes to Handle 2D Coordinate Scenarios

This module supports the following functionalities:

- Create and view 2D coordinates
- Find the distance between two coordinates
- Find the distance of a coordinate from the origin
- Check if a point lies on a given line
- Find the distance between a 2D point and a given line
"""
class Point:
    def __init__(self,x,y):
        self.x_cord = x
        self.y_cord = y
    
    def __str__(self):
        return "<{},{}>".format(self.x_cord, self.y_cord)
    
    def euclidean_distance(self,other):
        return ((self.x_cord - other.x_cord)**2 + (self.y_cord - other.y_cord)**2)**0.5
    
    def distance_from_origin(self):
        return self.euclidean_distance(Point(0,0))


p1 = Point(10,10)
p2 = Point(10,10)
dis = p1.euclidean_distance(p2)
print(dis)
dis_origin = p1.distance_from_origin()
print(dis_origin)