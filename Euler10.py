# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 11:05:23 2020

@author: stefflc

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.


"""

'''
BAse on wikipedia pseudo code
function is_prime(n)
    if n ≤ 3 then
        return n > 1
    else if n mod 2 = 0 or n mod 3 = 0
        return false

    let i ← 5

    while i × i ≤ n do
        if n mod i = 0 or n mod (i + 2) = 0
            return false
        i ← i + 6

    return true

'''

def isPrime(x):
    if x<=3:
        return x>1
    elif(x % 2 == 0):
        return False
    elif(x % 3 == 0):
        return False

    y = 5

    while(y*y <= x):
        if(x % y == 0 or x%(y+2) == 0):
            return False
        y = y +6
    return True



sum = 0

for x in range(1, 2000000):
    # print("%s isPrime(x)? %s"%(x, isPrime(x)))
    if(isPrime(x)):
        sum = sum+ x

print("sum: ", sum)
#Answer 142913828922

