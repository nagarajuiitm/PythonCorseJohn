# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 16:40:49 2019

@author: SNR
"""

class parent():
    
    def print_last_name(self):
        print("Banavatula")
        
class child(parent):
    
    def print_first_name(self):
        print("john")
        
    def print_last_name(self):
        print('Bhukya')
        
John = child()
John.print_last_name()
John.print_first_name()
