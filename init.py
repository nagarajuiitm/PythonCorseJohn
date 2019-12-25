# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 15:17:42 2019

@author: SNR
"""

class Tuna:
    
    def __init__(self):
        print("john")
        
    def swim(self):
        print("I am swiming")
        
fliper = Tuna()
fliper.swim()

class Enemy:
    def __init__(self, x):
        self.energy = x 
        
    def get_energy(self):
        print(self.energy)
        
jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()