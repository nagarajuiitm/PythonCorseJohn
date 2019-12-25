# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:21:14 2019

@author: SNR
"""

def allowed_dating_age(my_age):
    girls_age = my_age / 2 + 7
    return girls_age;

Buckys_limit = allowed_dating_age(27)
Creepy_joe_limit = allowed_dating_age(40)
print("Bucky can date girls" , Buckys_limit, "or older")
print("Creepy joe can date girls" , Creepy_joe_limit, "or older")
