# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 15:32:36 2019

@author: SNR
"""

classmates = {'Tony':'cool but smells', 'Emma':'sits behind me', 'Lucy':'asks too many questions'}

print(classmates)
print(classmates['Lucy'])

for key,value in classmates.items():
    print(key, value)
    print(key + value)