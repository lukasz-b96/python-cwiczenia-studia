#!/usr/bin/env python
# -*- coding: utf-8 -*-

def factorial(n):
    out = 1
    while n >= 1:
        out *= n
        n -= 1
    print(out)


for i in range(7):
    factorial(i)
