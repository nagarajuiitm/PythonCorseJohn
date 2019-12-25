# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 11:27:09 2019

@author: SNR
"""

while True:
    try:
        number = int(input("What is your favourite number?\n"))
        print(18/number)
    except ValueError:
        print("Make sure and a enter number")
    except NameError:
        print("Don't enter a name")
    except ZeroDivisionError:
        print("Don not pick up zero")
    except:
        break
    finally:
        print("loop complete")
        
    
        
 