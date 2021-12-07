#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# 1
dict1 = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90, 'C':100, 'CD':400, 'D':500, 'CM':900, 'M':1000}

# 2
dict2 = dict(I=1, IV=4, V=5, IX=9, X=10, XL= 40, L= 50, XC=90, C=100, CD=400, D= 500, CM=900, M=1000)

# 3
dict3 = {}
dict3['I'] = 1
dict3['IV'] = 4
dict3['V'] = 5
dict3['IX'] = 9
dict3['X'] = 10
dict3['XL'] = 40
dict3['L'] = 50
dict3['XC'] = 90
dict3['C'] = 100
dict3['CD'] = 400
dict3['D'] = 500
dict3['CM'] = 900
dict3['M'] = 1000

# 4
D = dict([("I",1), ("V",5)])

# 5
keys = ["I", "V", "X"]
vals = [1, 5, 10]
zipper = dict(zip(keys,vals))


print(dict1)
print(dict2)
print(dict3)
print(D)
print(zipper)

def roman2int(s):
    i = 0
    num = 0
    while i < len(s):
        if i+1<len(s) and s[i:i+2] in dict1:
            num += dict1[s[i:i+2]]
            i+=2
        else:
            num += dict1[s[i]]
            i+=1
    return num

print(roman2int('CDXLIII'))
print(roman2int('XXL'))
print(roman2int('XL'))
print(roman2int('LX'))