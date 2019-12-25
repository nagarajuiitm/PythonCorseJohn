# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:56:39 2019

@author: SNR
"""
from operator import itemgetter

users = [{'fname': 'Bucky', 'lname': 'Roberts'},
         {'fname': 'Tom', 'lname': 'Roberts'},
         {'fname': 'Bernie', 'lname': 'Zunks'},
         {'fname': 'Jenna', 'lname': 'Hayes'},
         {'fname': 'Sally', 'lname': 'Jones'},
         {'fname': 'Amada', 'lname':'Roberts'},
         {'fname': 'Tom', 'lname': 'Williams'},
         {'fname': 'Dean', 'lname': 'Hayes'},
         {'fname': 'Bernie', 'lname': 'Barbie'},
         {'fname': 'Tom', 'lname': 'Jones'}]

print(users)

for x in sorted(users, key=itemgetter('lname')):
    print(x)
    
print('______')

for x in sorted(users, key=itemgetter('fname', 'lname')):
    print(x)