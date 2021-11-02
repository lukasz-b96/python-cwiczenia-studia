#!/usr/bin/env python
# -*- coding: utf-8 -*-

def odwracanie_iteracyjne(lista):
    # najchetniej bym uzyl lista[::-1]
    # lub reversed()
    # lub .reverse()
    max_index = len(lista)
    for i in range(0, int(max_index/2), 1):
        temp = lista[i]
        lista[i] = lista[max_index - i - 1]
        lista[max_index - i - 1] = temp
    print(lista)


def odwracanie_rekurencyjne(lista):
    if not lista:
        return lista
    return lista[-1:] + odwracanie_rekurencyjne(lista[:-1])


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # parzyste
lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  # nieparzyste

odwracanie_iteracyjne(lista)
odwracanie_iteracyjne(lista2)


print(odwracanie_rekurencyjne(lista))
print(odwracanie_rekurencyjne(lista2))
