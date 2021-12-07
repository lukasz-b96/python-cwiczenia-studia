#!/usr/bin/env python
# -*- coding: utf-8 -*- 

while(True):
    try:
        data = input()
        if (data == 'stop'):
            break
        data = float(data)
    except ValueError:

        print('This is not a float!')
        continue
    print(data, data ** 3)