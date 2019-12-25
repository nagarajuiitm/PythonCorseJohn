# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:15:50 2019

@author: SNR
"""

from operator import attrgetter

class user:
    
    def __init__(self, x, y):
        self.name = x 
        self.user_id = y
        
    def __repr__(self):
        return self.name + " : " + str(self.user_id)
    
users = [user('Bucky', 87),
        user('Sally', 7),
        user('Tuna', 61),
        user('Brian', 2),
        user('Joby', 77),
        user('Amanda', 9)]

for user in users:
    print(user)
    
print('________')

for user in sorted(users, key=attrgetter('name')):
    print(user)
    
print('______')

for user in sorted(users, key=attrgetter('user_id')):
    print(user)