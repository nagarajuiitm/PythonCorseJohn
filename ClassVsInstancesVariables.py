# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:13:59 2019

@author: SNR
"""

class Giril:
    
    gender = 'female'
    
    def __init__(self, name):
        self.name = name
        
r = Giril('sunitha')
s = Giril('Anusha')

print(r.gender)
print(s.gender)
print(r.name)
print(s.name)

print('sunitha is a :', r.gender)
print('Anusha is a :', s.gender)
print('My name is :', r.name)