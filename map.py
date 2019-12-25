# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:32:31 2019

@author: SNR
"""

income = [10, 30, 75]

def double_money(dollars):
    return dollars * 2 

new_income = list(map(double_money, income))
print(new_income)

for x in income:
    print(x * 2)