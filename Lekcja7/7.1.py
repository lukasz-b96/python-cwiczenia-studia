#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
import unittest


def least_common_multiple(a, b):
    return abs(a * b) // math.gcd(a, b)


def to_common_denominator(my_self, my_other):
    y = least_common_multiple(my_self.y, my_other.y)
    x1 = my_self.x * (y / my_self.y)
    x2 = my_other.x * (y / my_other.y)
    return Frac(x1, y), Frac(x2, y)


class Frac:
    # Klasa reprezentująca ułamki.

    def __init__(self, x=0, y=1):

        if y == 0:
            raise ValueError("zero w mianowniku")

        self.x = x
        self.y = y

    def __str__(self):
        # x/y'.
        if self.y == 1:
            return "{0}".format(self.x)
        else:
            return "{0}/{1}".format(self.x, self.y)

    def __repr__(self):
        # return Frac(x, y)
        return "Frac({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        # my_self == my_other
        my_self, my_other = to_common_denominator(self, other)
        return my_self.x == my_other.x

    def __ne__(self, other):
        # my_self != my_other
        return not self == other

    def __lt__(self, other):
        # my_self < my_other
        my_self, my_other = to_common_denominator(self, other)
        return my_self.x < my_other.x

    def __le__(self, other):
        # my_self <= my_other
        my_self, my_other = to_common_denominator(self, other)
        return my_self.x <= my_other.x

    def __gt__(self, other):
        # my_self > my_other
        my_self, my_other = to_common_denominator(self, other)
        return my_self.x > my_other.x

    def __ge__(self, other):
        # my_self >= my_other
        my_self, my_other = to_common_denominator(self, other)
        return my_self.x >= my_other.x

    def __add__(self, other):
        if isinstance(other, Frac):
            # my_self + my_other
            y = least_common_multiple(self.y, other.y)
            x = self.x * (y / self.y) + other.x * (y / other.y)
            return Frac(x, y)
        elif isinstance(other, int):
            # my_self + int
            x = self.x + other * self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(other, float):
            # my_self + float
            a, b = other.as_integer_ratio()
            y = least_common_multiple(self.y, b)
            x = self.x * (y / self.y) + a * (y / b)
            return Frac(x, y)

    # int+frac
    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac):
            # my_self - my_other
            y = least_common_multiple(self.y, other.y)
            x = self.x * (y / self.y) - other.x * (y / other.y)
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, int):
            # my_self - int
            x = self.x - other * self.y
            y = self.y
            return Frac(x, y)
        elif isinstance(self, Frac) and isinstance(other, float):
            # my_self - float
            a, b = other.as_integer_ratio()
            y = least_common_multiple(self.y, b)
            x = self.x * (y / self.y) - a * (y / b)
            return Frac(x, y)

    def __rsub__(self, other):
        # int-frac, tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac):
            # my_self * my_other
            x = self.x * other.x
            y = self.y * other.y
            gcd = math.gcd(x, y)
            return Frac(x // gcd, y // gcd)
        elif isinstance(self, Frac) and isinstance(other, int):
            # my_self * int
            x = self.x * other
            y = self.y
            gcd = math.gcd(x, y)
            return Frac(x // gcd, y // gcd)
        elif isinstance(self, Frac) and isinstance(other, float):
            # my_self * float
            a, b = other.as_integer_ratio()
            x = self.x * a
            y = self.y * b
            gcd = math.gcd(x, y)
            return Frac(x // gcd, y // gcd)

    # int*frac
    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(self, Frac) and isinstance(other, Frac):
            # my_self / my_other
            return self * ~other
        elif isinstance(self, Frac) and isinstance(other, int):
            # my_self / int
            return self * Frac(1, other)
        elif isinstance(self, Frac) and isinstance(other, float):
            # my_self / float
            a, b = other.as_integer_ratio()
            return self * Frac(b, a)
        else:
            return Frac()  # error?

    def __rtruediv__(self, other):
        # int/frac
        return other * ~self

    def __pos__(self):
        # +frac = (+1)*frac
        return self

    def __neg__(self):
        # -frac = (-1)*frac
        return -1 * self

    def __invert__(self):
        #odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __float__(self):
        # float(frac)
        return self.x / self.y


class TestFrac(unittest.TestCase):

    def test_set_up(self):
        self.zero = Frac()

    def test_zero_denominator(self):
        self.assertRaises(ValueError, Frac, 1, 0)

    def test_print_all(self):
        self.assertEqual(str(Frac(2, 6)), "2/6")
        self.assertEqual(repr(Frac(2, 6)), "Frac(2, 6)")

    def test_compare(self):
        self.assertTrue(Frac(2, 6) < Frac(7, 4))
        self.assertTrue(Frac(2, 6) <= Frac(7, 4))
        self.assertTrue(Frac(2, 6) <= Frac(2, 6))
        self.assertTrue(Frac(2, 6) > Frac(1, 6))
        self.assertTrue(Frac(2, 6) >= Frac(2, 6))
        self.assertTrue(Frac(2, 6) == Frac(1, 3))
        self.assertTrue(Frac(2, 6) == Frac(2, 6))
        self.assertTrue(Frac(2, 6) != Frac(1, 6))

    def test_add_fracfrac(self):
        self.assertEqual(Frac(1, 2) + Frac(1, 3), Frac(5, 6))

    def test_add_fracint(self):
        self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))

    def test_add_intfrac(self):
        self.assertEqual(1 + Frac(1, 2), Frac(3, 2))

    def test_add_fracfloat(self):
        self.assertEqual(Frac(1, 3) + 1.5, Frac(11, 6))

    def test_sub_fracfrac(self):
        self.assertEqual(Frac(1, 2) - Frac(1, 3), Frac(1, 6))

    def test_sub_fracint(self):
        self.assertEqual(Frac(1, 2) - 1, Frac(-1, 2))

    def test_sub_intfrac(self):
        self.assertEqual(1 - Frac(1, 2), Frac(1, 2))

    def test_sub_fracfloat(self):
        self.assertEqual(Frac(2, 3) - 0.5, Frac(1, 6))

    def test_mul_fracfrac(self):
        self.assertEqual(Frac(2, 3) * Frac(3, 4), Frac(1, 2))

    def test_mul_fracint(self):
        self.assertEqual(Frac(2, 3) * 2, Frac(4, 3))

    def test_mul_intfrac(self):
        self.assertEqual(2 * Frac(2, 3), Frac(4, 3))

    def test_mul_fracfloat(self):
        self.assertEqual(Frac(2, 5) * 1.5, Frac(3, 5))

    def test_div_fracfrac(self):
        self.assertEqual(Frac(2, 3) / Frac(3, 4), Frac(8, 9))

    def test_div_fracint(self):
        self.assertEqual(Frac(2, 3) / 2, Frac(1, 3))

    def test_div_intfrac(self):
        self.assertEqual(2 / Frac(3, 4), Frac(8, 3))

    def test_div_fracfloat(self):
        self.assertEqual(Frac(2, 3) / 0.5, Frac(4, 3))

    def test_single_arguments(self):
        self.assertEqual(+Frac(2, 3), Frac(2, 3))
        self.assertEqual(+Frac(2, 3), Frac(-2, -3))
        self.assertEqual(-Frac(2, 3), Frac(-2, 3))
        self.assertEqual(-Frac(2, 3), Frac(2, -3))
        self.assertEqual(~Frac(2, 3), Frac(3, 2))

    def test_float_frac(self):
        self.assertEqual(float(Frac(2, 3)), 2/3)

    def test_tearDown(self): 
        pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
