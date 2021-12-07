#!/usr/bin/env python
# -*- coding: utf-8 -*- 

box=''
row, col = 2, 4

assert row >= 1, 'bad row size' 
assert col >= 1, 'bad col size' 


for w in range(row):
    box += '+'
    for l in range(col):
        box += '---+'
    box += '\n|'
    for l in range(col):
        box += '   |'
    box += '\n'
box += '+'
for l in range(col):
    box += '---+'
    
print(box)