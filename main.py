from decimal import Decimal
import decimal


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

        # 两直线平行
        if self.is_vertical() and line2.is_vertical():
            return None

        if self.k == line2.k:
            return None

        # 相交

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
        r1 = (self.p2.x, self.p1.x) if self.p1.x >= self.p2.x else (self.p1.x, self.p2.x)
        r2 = (line2.p2.x, line2.p1.x) if line2.p1.x >= line2.p2.x else (line2.p1.x, line2.p2.x)
        if not (r1[0] <= x <= r1[1] and r2[0] <= x <= r2[1]):
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
            self.lines.append(Line(points[i], points[i+1]))


    def contains(self, point):

        point_b = Point(point.x+100000000, point.y) # 这个值尽量大，因为暂时不支持射线

        line2 = Line(point, point_b)
        line3 = Line(Point(2, -1), Point(2, 3))

        return len(list(filter(lambda p: p is not None, list(map(lambda l: l.intersection(line2), self.lines))))) % 2 == 1






if __name__ == "__main__":


    # 区域是南昌大学前湖校区，点是区域里的一点
    poly = Polygen(Point(Decimal('28.6595744800'), Decimal('115.8178412500')), Point(Decimal('28.6704640100'), Decimal('115.8110525800')), 
        Point(Decimal('28.6657077700'), Decimal('115.7966829800')), Point(Decimal('28.6427316600'),Decimal('115.7875711800')),
        Point(Decimal('28.6396932200'), Decimal('115.7987466100')), Point(Decimal('28.6588107300'), Decimal('115.8179824100')))
    print(poly.contains(Point(Decimal('28.6577095300'), Decimal('115.8007106600'))))


    # p = Point(0.5, -0.5)
    # points = [(-3, 0), (0, 4), (2, 0), (0, -2), (-2, -1)]

    # poly = Polygen(*[Point(e[0], e[1]) for e in points])
    # print(poly.contains(p))


    # l1 = Line(Point(2, 0), Point(0, -2))
    # l2 = Line(Point(0.5, -0.5), Point(10000, -0.5))
    # print(l1.intersection(l2))




