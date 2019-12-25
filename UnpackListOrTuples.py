# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 15:12:31 2019

@author: SNR
"""

item = ['December 23, 2015', 'Bread Gloves', 8.15]
print(item)

date, name, price = ['December 23, 2015', 'Bread Gloves', 8.15]
print(name)
print(price)

def drop_first_last(grades):
    first, *middle, last = grades
    avg = sum(middle) / len(middle)
    print(avg)
    
drop_first_last([25, 65, 79, 50, 68, 89])
drop_first_last([67, 78, 35, 73, 55, 84, 45, 65, 64, 57, 99])

