import unittest
from points import Point


class Rectangle:
    """Klasa reprezentująca prostokąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
        if x1 >= x2 or y1 >= y2:
            raise ValueError("# Chcemy, aby x1 < x2, y1 < y2.")
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        # "[(x1, y1), (x2, y2)]"
        return f"[{self.pt1.x, self.pt1.y}, {self.pt2.x, self.pt2.y}]"

    def __repr__(self):
        # "Rectangle(x1, y1, x2, y2)"
        return f"Rectangle({self.pt1.x}, {self.pt1.y}, {self.pt2.x}, {self.pt2.y})"

    def __eq__(self, other):
        # obsługa rect1 == rect2
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        # zwraca środek prostokąta
        return (Point((self.pt1.x + self.pt2.x)/2, (self.pt1.y + self.pt2.y)/2))

    def area(self):
        # pole powierzchni
        return abs(self.pt2.x - self.pt1.x) * abs(self.pt2.y - self.pt1.y)

    def move(self, x, y):
        x1 = self.pt1.x + x
        y1 = self.pt1.y + y
        x2 = self.pt2.x + x
        y2 = self.pt2.y + y
        return Rectangle(x1, y1, x2, y2)

    def intersection(self, other):
        x1 = max(self.pt1.x, other.pt1.x)
        y1 = max(self.pt1.y, other.pt1.y)
        x2 = min(self.pt2.x, other.pt2.x)
        y2 = min(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def cover(self, other):
        x1 = min(self.pt1.x, other.pt1.x)
        y1 = min(self.pt1.y, other.pt1.y)
        x2 = max(self.pt2.x, other.pt2.x)
        y2 = max(self.pt2.y, other.pt2.y)
        return Rectangle(x1, y1, x2, y2)

    def make4(self):
        # zwraca krotkę czterech mniejszych
        center = self.center()
        x3, y3 = center.x, center.y
        r1 = Rectangle(self.pt1.x,y3,x3,self.pt2.y)
        r2 = Rectangle(x3, y3, self.pt2.x, self.pt2.y)
        r3 = Rectangle(self.pt1.x, self.pt1.y, x3, y3)
        r4 = Rectangle(x3, self.pt1.y, self.pt2.x, y3)
        return (r1,r2,r3,r4)
# A-------B   po podziale  A---+---B       x1,y2 --- x3,y2 --- x2,y2
# |       |                |   |   |         |        |          |
# |       |                +---+---+       x1,y3 --- x3,y3 --- x2,y3
# |       |                |   |   |         |        |          |
# D-------C                D---+---C       x1,y1 --- x3,y1 --- x2,y1

# Kod testujący moduł.


class TestRectangle(unittest.TestCase):
    def test_set_up(self):
        pass

    def test_create(self):
        # self.assertRaises(ValueError,Rectangle(0,1,4,0))
        # self.assertRaises(ValueError,Rectangle(5,1,0,0))
        self.assertRaises(ValueError, Rectangle, 5, 1, 0, 3)

    def test_str(self):
        self.assertEqual("[(2, 0), (4, 1)]", str(Rectangle(2, 0, 4, 1)))

    def test_rep(self):
        self.assertEqual("Rectangle(1, 2, 3, 4)", repr(Rectangle(1, 2, 3, 4)))

    def test_eq(self):
        self.assertTrue(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4))
        self.assertTrue(Rectangle(1, 2, 3, 4) != Rectangle(5, 5, 6, 6))

    def test_center(self):
        self.assertEqual(Rectangle(0, 4, 2, 6).center(), Point(1, 5))
        self.assertEqual(Rectangle(-4, -1, 2, 0).center(), Point(-1, -0.5))

    def test_area(self):
        self.assertEqual(Rectangle(0, 0, 4, 6).area(), 24)
        self.assertEqual(Rectangle(-2, 1, 4, 3).area(), 12)

    def test_move(self):
        self.assertEqual(Rectangle(-2, -2, 1, 1).move(3, -2),
                         Rectangle(1, -4, 4, -1))
        self.assertTrue(Rectangle(0, 0, 1, 1).move(
            3, -2) == Rectangle(3, -2, 4, -1))

    def test_intersection(self):
        self.assertEqual(
            Rectangle(-2, -4, 4, 5).intersection(Rectangle(0, 0, 3, 3)), Rectangle(0, 0, 3, 3))
        self.assertEqual(
            Rectangle(-2, -4, 4, 5).intersection(Rectangle(0, 0, 10, 10)), Rectangle(0, 0, 4, 5))

    def test_cover(self):
        self.assertEqual(
            Rectangle(-2, -4, 4, 5).cover(Rectangle(0, 0, 3, 3)), Rectangle(-2, -4, 4, 5))
        self.assertEqual(
            Rectangle(-2, -4, 4, 5).cover(Rectangle(0, 0, 10, 10)), Rectangle(-2, -4, 10, 10))
    def test_make4(self):
        self.assertEqual(Rectangle(0,0,10,6).make4(),(
            Rectangle(0,3,5,6), 
            Rectangle(5,3,10,6),
            Rectangle(0,0,5,3),
            Rectangle(5,0,10,3)
        ))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
