# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:35:49 2019

@author: SNR
"""

answer = lambda x: x*7
print(answer(5))


remainder = lambda num: num % 2
print(remainder(5))

def remainder(num):
    return num % 2
print(remainder(5))

product = lambda x, y: x * y 
print(product(2, 4))

def testfunc(num):
    return lambda x: x * num

result1 = testfunc(8)
result2 = testfunc(3)
print(result1(2))
print(result2(4))