# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:23:55 2019

@author: SNR
"""

def printInput(inputData):    
    return inputData;   
    
def printInput(inputData,data2):    
    return inputData+data2;

def printInput(inputData,data2):    
    return inputData;


printInput("ABC",2)
printInput(2.0,3)

class Mario():
    
    def move(self):
        print('I am moving')
        
class Shroom():
    
    def eat_shroom(self):
        print('Now I am big!')
        
class BigMario(Mario, Shroom):
    pass


bm = BigMario()
bm.move()
bm.eat_shroom()    