#!/usr/bin/env python
# -*- coding: utf-8 -*- 

arr = [[],[4],(1,2),[3,4],(5,6,7)]
output = []
for el in arr:
    if type(el) is tuple:
        output.append(sum(list(el)))
    elif type(el) is list:
        output.append(sum(el))
    else:
        print('error')
        exit()
print(output)
        