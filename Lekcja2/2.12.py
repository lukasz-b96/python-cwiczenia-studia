#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

line = 'Lorem ipsum dolor sit amet, ' \
    'consectetur adipiscing elit.\n' \
    'Aliquam accumsan sem eu ante facilisis posuere.\n' \
    'Morbi euismod malesuada diam, ' \
    'quis porttitor elit venenatis sed.\n' \
    'Pellentesque suscipit eget erat sed egestas.\n' \
    'Ut rhoncus massa eget arcu laoreet imperdiet.\n' \
    'Sed sit amet gravida eros.\n' \
    'Maecenas auctor mollis mi eget ultrices.\n' \
    'Quisque viverra pulvinar neque,\t \
    nec fringilla risus semper eget.'
    
split = line.split()
pierwsze = ''.join([first[0] for first in split])
ostatnie = ''.join(last[-1:] for last in split)
print("Wyraz stworzony z pierwszych znakow:", pierwsze)
print("Wyraz stworzony z ostatnich znakow:", ostatnie)
