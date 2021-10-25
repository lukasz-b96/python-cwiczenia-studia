#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# a) 
# kod poprawny, mozna usunac średniki i wtedy dla 
# x oraz y ustawić "pod sobą"
# mozna rowniez usunac nawiasy w if
# poprawione
x = 2
y = 3
if x > y:
    result = x
else:
    result = y
    
# b)
# kod niepoprawny skladniowo
# program nie  wykona sie
# trzeba przeniesc if do nowej lini oraz od musi byc od tabulatora
# print () mozna zamienic na print() dla pythona3 
# print mozna przeniesc do kolejnej linii od tabulatora
# poprawione
for i in "qwerty": 
    if ord(i) < 100: 
        print(i)

# c)
# kod poprawny skladniowo dla python2
# mozna zamienic print () na print() dla pythona3
# poprawione
for i in "axby": 
    print(ord(i) if ord(i) < 100 else i) 