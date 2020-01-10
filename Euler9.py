# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:47:53 2020

@author: stefflc


A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


"""
import math

for x in range(1, 500):
    for y in range(1, 500):
        a = math.pow(x, 2)
        b = math.pow(y, 2)
        c = a+ b

        if (( x + y + math.sqrt(c) == 1000) and (x <y) and (y < math.sqrt(c))):
            print("winner", x, y, math.sqrt(c))
            print("sum of a*b*c: ", x*y*math.sqrt(c))




