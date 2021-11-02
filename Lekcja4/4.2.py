#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_ruler(n):

    DOTS = '....'

    val = n

    for i in range(val):
        print('|' + DOTS, end='')

    print('|')
    print('0', end=' ')

    for i in range(1, val + 1):
        print(str(i).rjust((len(DOTS))), end=' ')
    print('')


def make_grid(rows, cols):
    assert rows >= 1, 'bad rowsss size'
    assert cols >= 1, 'bad col size'

    box = ''
    for w in range(rows):
        box += '+'
        for l in range(cols):
            box += '---+'
        box += '\n|'
        for l in range(cols):
            box += '   |'
        box += '\n'
    box += '+'
    for l in range(cols):
        box += '---+'

    print(box)


n = 11
r = 3
c = 4
make_ruler(n)
make_grid(r, c)
