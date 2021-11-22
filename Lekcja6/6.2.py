#!/usr/bin/env python
# -*- coding: utf-8 -*-

from points import *
import unittest
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __repr__(self):
        return "Point({0}, {1})".format(self.x, self.y)

    def __eq__(self, second):
        return self.x == second.x and self.y == second.y

    def __ne__(self, second):
        return not self == second

    def __add__(self, second):
        return Point(self.x + second.x, self.y + second.y)

    def __sub__(self, second):
        return Point(self.x - second.x, self.y - second.y)

    def __mul__(self, second):
        return Point(self.x * second.x, self.y * second.y)

    def cross(self, second):
        return self.x * second.y - self.y * second.x

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)


class TestPoint(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Point(5, 2)), "(5, 2)")
        self.assertEqual(repr(Point(5, 2)), "Point(5, 2)")

    def test_cmp(self):
        self.assertTrue(Point(1, 2) == Point(1, 2))
        self.assertTrue(Point(1, 5) != Point(3, 2))
        self.assertTrue(Point(1, 2) != Point(1, 3))
        self.assertTrue(Point(7, 2) != Point(5, 5))

    def test_add(self):
        self.assertEqual(Point(1, 2) + Point(3, 6), Point(4, 8))
        self.assertEqual(Point(3, 2) + Point(-1, 6), Point(2, 8))

    def test_subtract(self):
        self.assertEqual(Point(4, 1) - Point(2, 1), Point(2, 0))
        self.assertEqual(Point(-2, 1) - Point(4, 2), Point(-6, -1))

    def test_scalar(self):
        self.assertEqual(Point(4, 2) * Point(2, 1), Point(8, 2))

    def test_cross(self):
        self.assertEqual(Point(4, 1).cross(Point(3, 2)), 5)

    def test_len(self):
        self.assertEqual(Point(4, 3).length(), 5)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
