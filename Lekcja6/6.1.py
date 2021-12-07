#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from times import *


class Time:
    def __init__(self, s=0):
        if s < 0:
            raise ValueError("ujemny czas")
        self.s = int(s)

    def __str__(self):
        h = self.s // 3600
        sec = self.s - h * 3600
        m = sec // 60
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        return "Time({})".format(self.s)

    def __add__(self, other):
        return Time(self.s + other.s)

    # def __cmp__(self, other): # Py2, porównywanie, -1|0|+1
    #    """Porównywanie odcinków czasu."""
    #    return cmp(self.s, other.s)

    def __eq__(self, other):
        return self.s == other.s

    def __ne__(self, other):
        return self.s != other.s

    def __lt__(self, other):
        return self.s < other.s

    def __le__(self, other):
        return self.s <= other.s

    # nadmiarowe
    # def __gt__(self, other):
    #    return self.s > other.s

    # nadmiarowe
    # def __ge__(self, other):
    #    return self.s >= other.s

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s


class TestTime(unittest.TestCase):

    def setUp(self): pass

    def test_print(self):
        self.assertEqual(str(Time(10)), "00:00:10")
        self.assertEqual(repr(Time(4)), "Time(4)")

    def test_add(self):
        self.assertEqual(Time(1) + Time(2), Time(3))
        self.assertEqual(Time(4) + Time(4), Time(8))
        self.assertEqual(Time(6) + Time(6), Time(12))

    def test_cmp(self):
        self.assertTrue(Time(1) == Time(1))
        self.assertTrue(Time(6) == Time(6))
        self.assertTrue(Time(8) == Time(8))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(1) != Time(2))
        self.assertTrue(Time(3) > Time(2))
        self.assertTrue(Time(2) < Time(3))
        self.assertTrue(Time(4) < Time(5))
        self.assertTrue(Time(2) >= Time(2))
        self.assertTrue(Time(3) >= Time(3))
        self.assertTrue(Time(3) >= Time(2))
        self.assertTrue(Time(5) >= Time(5))

    def test_int(self):
        self.assertEqual(int(Time(3600)), 3600)

    def tearDown(self): pass


if __name__ == "__main__":
    unittest.main()
