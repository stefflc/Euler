# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 13:43:04 2020

@author: stefflc


The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?


"""
def findTriangle(x):
    if(x==1):
        return 1
    elif(x==2):
        return 3
    else:
        return(x + findTriangle(x-1))

def findDivisors(x):
    divisorlist = list()
    divisorlist.append(x)

    test = x
    while(test % 2 == 0):
        if(test not in divisorlist):
            divisorlist.append(test)
        test = test /2
        findDivisors(test)
        # factor = test / 2
        # if(factor not in divisorlist):
        #     divisorlist.append(factor)
        # test = factor
    print("div list: ", divisorlist)


for x in range(1, 8):
    tri = findTriangle(x)
    print(tri)
    findDivisors(tri)