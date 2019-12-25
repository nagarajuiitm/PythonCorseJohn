# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:40:23 2019

@author: SNR
"""

def get_gender(sex="unknown"):
    if sex is 'M':
        sex = 'Male'
    elif sex is 'F':
        sex = 'Female'
    print(sex)
    
get_gender('M')
get_gender('F')
get_gender()