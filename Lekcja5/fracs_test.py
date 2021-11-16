#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from fracs import *


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([3, 4], [1, 2]), [5, 4])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([3, 4], [1, 2]), [1, 4])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([3, 4], [1, 2]), [3, 8])
        self.assertEqual(mul_frac([3, 4], [2, 1]), [3, 2])
        self.assertEqual(mul_frac([3, 6], [3, 2]), [3, 4])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([3, 4], [1, 2]), [3, 2])
        self.assertEqual(div_frac([3, 4], [2, 1]), [3, 8])
        self.assertEqual(div_frac([3, 6], [3, 2]), [1, 3])

    def test_is_positive(self):
        self.assertEqual(is_positive([1, 2]), True)
        self.assertEqual(is_positive([-1, -2]), True)
        self.assertEqual(is_positive([1, -2]), False)
        self.assertEqual(is_positive([-1, 2]), False)

    def test_is_zero(self):
        self.assertEqual(is_zero([0, 2]), True)
        self.assertEqual(is_zero([0, -2]), True)
        self.assertEqual(is_zero([1, -2]), False)
        self.assertEqual(is_zero([-1, 2]), False)

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), -1)
        self.assertEqual(cmp_frac([1, 2], [2, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, 3]), 1/3)
        self.assertEqual(frac2float([5, 4]), 5/4)
        self.assertEqual(frac2float([5, 4]), 1.25)

    def tearDown(self): pass


if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
