#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math


def least_common_multiple(a, b):
    return abs(a * b) // math.gcd(a, b)


def greatest_common_divisor(a, b):
    return math.gcd(a, b)


def add_frac(frac1, frac2):     # frac1 + frac2
    denominator = least_common_multiple(frac1[1], frac2[1])
    numerator = frac1[0] * (denominator / frac1[1]) + \
        frac2[0] * (denominator / frac2[1])
    return [numerator, denominator]


def sub_frac(frac1, frac2):     # frac1 - frac2
    denominator = least_common_multiple(frac1[1], frac2[1])
    numerator = frac1[0] * (denominator / frac1[1]) - \
        frac2[0] * (denominator / frac2[1])
    return [numerator, denominator]


def mul_frac(frac1, frac2):     # frac1  *  frac2
    denominator = frac1[1] * frac2[1]
    numerator = frac1[0] * frac2[0]
    gcd = greatest_common_divisor(numerator, denominator)
    return [numerator / gcd, denominator / gcd]


def div_frac(frac1, frac2):     # frac1 / frac2
    denominator = frac1[1] * frac2[0]
    numerator = frac1[0] * frac2[1]
    gcd = greatest_common_divisor(numerator, denominator)
    return [numerator / gcd, denominator / gcd]


def is_positive(frac):          # bool, czy dodatni
    return (frac[0] > 0 and frac[1] > 0) or (frac[0] < 0 and frac[1] < 0)


def is_zero(frac):              # bool, typu [0, x]
    return frac[0] == 0


def cmp_frac(frac1, frac2):     # -1 | 0 |  + 1
    denominator = least_common_multiple(frac1[1], frac2[1])
    numerator1 = frac1[0] * (denominator / frac1[1])
    numerator2 = frac2[0] * (denominator / frac2[1])

    if numerator1 > numerator2:
        return -1
    elif numerator2 > numerator1:
        return 1
    else:
        return 0


def frac2float(frac):           # konwersja do float
    return float(frac[0] / frac[1])
