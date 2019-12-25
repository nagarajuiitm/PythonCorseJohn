# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:32:32 2019

@author: SNR
"""

import heapq

grades = [43, 52, 56, 632, 663, 234, 732, 23, 876]
print(grades)
print(heapq.nlargest(4, grades))

stocks = [{'ticker': 'APPL', 'price': 201},
           {'ticker': 'F', 'price': 54},
          { 'ticker': 'MSFT', 'price': 313},
           {'ticker': 'TUNA', 'price': 68}]

print(heapq.nsmallest(2, stocks, key= lambda stock: stock['price']))