# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:33:34 2019

@author: SNR
"""

from struct import *
 
# store as bytes data
packed_data = pack('iif', 8, 6, 36.6)
print(packed_data)

print(calcsize('i'))
print(calcsize('f'))
print(calcsize('iif'))

# To gets bytes data back to normal b'\x08\x00\x00\x00\x06\x00\x00\x00ff\x12B'
original_data = unpack('iif', packed_data)
print(original_data)
print(unpack('iif', b'\x08\x00\x00\x00\x06\x00\x00\x00ff\x12B'))