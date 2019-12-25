# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 17:25:42 2019

@author: SNR
"""

fw = open('simple.txt', 'w')
TIOEd="""Reserve Bank of India deputy governor MK Jain yesterday asked banks to enhance their monitoring of small ticket size loans. He picked up the Mudra loans for emphasis and pointed out there have been concerns about the growing level of delinquencies among this group of borrowers. The deputy governor’s warning is just one more symptom of a fundamental problem of Indian banking.

Banks are the most important financial intermediaries in the economy and this sector is dominated by public sector entities. The last bad loan crisis has been attributed to, among other things, political interference in commercial decisions of banks. One of the consequences is that this political interference feeds into periodic crises in the financial sector."""
fw.write(TIOEd)
fw.close()

fr = open('simple.txt', 'r')
text = fr.read()
print(text)
fr.close()