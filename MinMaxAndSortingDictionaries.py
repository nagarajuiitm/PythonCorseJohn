# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:53:07 2019

@author: SNR
"""

stocks = {'GOOG' : 520.54, 
          'FB' : 76.45,
          'Yahoo': 39.29,
          'AMZN': 306.21,
          'AAPL': 99.26
}

print(stocks)
print(min(stocks))
print(min(zip(stocks.values(), stocks.keys())))
print(max(zip(stocks.values(), stocks.keys())))
print(sorted(zip(stocks.values(), stocks.keys())))
