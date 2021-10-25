#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import string

length = 20
letters = string.ascii_lowercase
random1 = set(''.join(random.choice(letters) for i in range(length + 1)))
random2 = set(''.join(random.choice(letters) for i in range(length + 1)))

print('random letters 1: ', list(random1))
print('random letters 2: ', list(random2))

print('a)', list(random1.intersection(random2)))
print('b)', list(random1.union(random2)))
