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

najdluzszy = max(line.split(), key=len)
print('a) Najdluzszy wyraz:', najdluzszy)
print('b) Dlugosc najdluzszego wyrazu:', len(najdluzszy))