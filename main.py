

class Point:

    def __init__(self, x, y):

        self.x = x;
        self.y = y;

    def __repr__(self):

        return "({},{})".format(self.x, self.y)

class Line:

    def __init__(self, p1, p2):

        self.p1 = p1
        self.p2 = p2

        self.k = (p2.y - p1.y)/(p2.x - p1.x) if p1.x != p2.x else None
        self.b = -p1.x*(p2.y-p1.y) / (p2.x-p1.x) + p1.y if p1.x != p2.x else None

    def intersection(self, line2):
        print("求交点: {0} + {1}".format(self, line2))

        # 两直线水平或垂直
        if (self.is_horizontal() and line2.is_horizontal()) or (self.is_vertical() and line2.is_vertical()):
            return None

        if self.k == line2.k:
            return None

        # 有其中一条垂直
        if self.is_vertical():
            x = self.p1.x
            y = round(line2.k*x + line2.b, 2)
        elif line2.is_vertical():
            x = line2.p1.x
            y = round(self.k*x + self.b, 2)
        else:
            # 一般情况
            x = round((self.b - line2.b)/(line2.k - self.k), 2)
            y = round(self.k*x + self.b, 2)

        # 点在线段上：x在线段的范围内
        if not (self.p1.x <= x <= self.p2.x and line2.p1.x <= x <= line2.p2.x):
            return None

        return Point(x, y)

        

    def is_horizontal(self):

        return self.p1.y == self.p2.y


    def is_vertical(self):

        return self.p1.x == self.p2.x


    def __repr__(self):
        return "[{}->{}, k={}, b={}]".format(self.p1, self.p2, self.k, self.b)


class Polygen:

    def __init__(self, *points):

        self.points = points
        self.lines = []
        for i in range(-1, len(points) - 1):
            print(i, i + 1)
            self.lines.append(Line(points[i], points[i+1]))


    def contains(self, point):

        point_b = Point(point.x+100000000, point.y) # 这个值尽量大，因为暂时不支持射线

        line2 = Line(point, point_b)
        line3 = Line(Point(2, -1), Point(2, 3))
        print(line2)
        print(line3)
        print(line2.intersection(line3))

        print(list(map(lambda l: l.intersection(line2), self.lines)))

        return len(list(filter(lambda p: p is not None, list(map(lambda l: l.intersection(line2), self.lines))))) % 2 == 1






if __name__ == "__main__":

    p = Point(100, 300)

    poly = Polygen(Point(-3, -2), Point(2, -1), Point(2, 3), Point(-100, 4))
    print(poly.contains(Point(-50, 1)))

    # l1 = Line(Point(-3, -2), Point(2, 3))
    # l2 = Line(Point(-3, -1), Point(2, -1))

    # print(l1.intersection(l2))
    # print(poly.contain(p))




