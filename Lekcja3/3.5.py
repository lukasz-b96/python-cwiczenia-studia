#!/usr/bin/env python
# -*- coding: utf-8 -*- 

DOTS = '....'

try:
    val = input()
    val = int(val)
    if val <= 0:
        exit()
except ValueError:
    exit()

for i in range(val):
    print('|' + DOTS, end='')
    
print('|')
print('0', end=' ')

for i in range(1, val + 1):
    print(str(i).rjust((len(DOTS))),end=' ')
print('')

