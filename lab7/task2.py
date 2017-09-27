import math


class Point:

    x = 0
    y = 0

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance_between_points(self, other_point):
        x_distance = abs(self.x - other_point.x)
        y_distance = abs(self.y - other_point.y)
        distance = math.pow(((x_distance**2 + y_distance**2)),0.5)
        return distance

    def add_with_point(self, other_point):
        new_x = self.x + other_point.x
        new_y = self.y + other_point.y
        return Point(new_x,new_y)

    def add_with_offset(self, offset):
        new_x = self.x + offset[0]
        new_y = self.y + offset[1]
        return Point(new_x,new_y)

    def __add__(self, other):
        if isinstance(other, tuple):
            return self.add_with_offset(other)
        else:
            return self.add_with_point(other)


def main():
    origin = Point(0,0)
    point1 = Point(1,1)
    print("Distance between origin and (1,1):", origin.distance_between_points(point1))
    ## adding two points
    new_point_1 = origin + point1
    print("New point_1:", new_point_1.x, new_point_1.y)
    ## adding a point with offset
    new_point_2 = origin + (1,1)
    print("New point_2:", new_point_2.x, new_point_2.y)



if __name__ == '__main__':
    main()