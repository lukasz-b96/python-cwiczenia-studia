#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fibonacci(n):
    a, b = 0, 1
    for i in range(0, n, 1):
        a, b = b, a + b
    print(a)


for i in range(7):
    fibonacci(i)
