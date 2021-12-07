#!/usr/bin/env python
# -*- coding: utf-8 -*-


def flatten(seq, suma=[]):
    for el in seq:
        if isinstance(el, (tuple, list)):
            flatten(el, suma)
        else:
            suma.append(el)
    return suma


lista = [1, 2, [], [3], [4, 5],
         ((), 6), (7), (8, 9), ((10), 11, 12, ((13), 14))]


print(flatten(lista))
