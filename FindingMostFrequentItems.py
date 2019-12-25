# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:11:38 2019

@author: SNR
"""

from collections import Counter

text = '''We can pass multiple iterable arguments to map() function, in that case, the specified function must have that many arguments. The function will be applied to these iterable elements in parallel. With multiple iterable arguments, the map iterator stops when the shortest iterable is exhausted.'''

words = text.split()
 
counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)



