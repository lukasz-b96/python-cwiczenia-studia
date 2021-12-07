#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# a) program niepoprawny poniewaz .sort() niczego nie zwraca i zastepuje L
# poprzez None
# mozna uzyc print(sorted(L) bez zmiany oryginalnej listy L) ktory zwroci posortowana liste 
# mozna rowniez uzyc samo L.sort() ktory zmieni liste L
# mozna usunac sredniki
# poprawione:
L = [3, 5, 4] 
# print(sorted(L)) # nie zmieni L
L.sort() # zmieni L
print('a)', L)


# b) niepoprawny poniewaz przypisuje 3 elementy tuple do 2 zmiennych
# poprawione 
x, y, z = 1, 2, 3
print('b)',x, y, z)

# c) "Tuples are unchangeable", można stworzyc tuple na nowow
# poprawione 
X = 1, 2, 3
X = X[0], 4, X[2]
print('c)',X)

# d) proba przypisania wartosci poza najwiekszym indeksem listy jest niemozliwa
# max index = 2 dla listy z 3 elementami
# mozna ewentualnie zmienic ostatni element, lub uzyc .append()
# poprawione 
X = [1, 2, 3]
# x[2] = 4 zmiana ostaniego elementu
X.append(4) 
print('d)',X)

# e) proba dodania elementu do listy poprzez append()
# w tym przypadku X nie jest lista i nalezy uzyc operatora przypisania
# poprawione 
X = "abc"
X += "d"
print('e)',X)

# f) brakuje drugiego argumentu w funkcji pow
# stworzyc wlasna funkcje ktora bedzie miala pewna wartosc domyslna
#poprawione

# sposob 1
def mypow(x,y=3):
    return x**y
L = list(map(mypow, range(8)))
print('f1)',L)

# sposob 2
power = 3
size = 8
P = list(map(lambda x,y: x**y, range(size), [power]*size))
print('f2)',P)
