# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 14:46:20 2019

@author: SNR
"""

from FlexibleNumberOfArguments import *

def health_calculator(age, apples_ate, crgs_smoked):
    answer = (100-age) + (apples_ate * 3.5) - (crgs_smoked * 2)
    print(answer)

   
Buckys_data = [27, 20, 0]
health_calculator(Buckys_data[0], Buckys_data[1], Buckys_data[2])
health_calculator(*Buckys_data)
