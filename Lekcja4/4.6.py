#!/usr/bin/env python
# -*- coding: utf-8 -*- 

def sum_seq(sequence):
    suma = 0
    for el in sequence:
        if isinstance(el, (tuple, list)):
            suma += sum_seq(el)
        else:
            suma += el
    return suma


lista = [1, 2, [], [3], [4, 5], ((),6), (7), (8, 9), ((10), 11, 12, ((13), 14))]



    
print(sum_seq(lista)) 