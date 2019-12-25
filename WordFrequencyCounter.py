# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 12:22:41 2019

@author: SNR
"""

import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    #url='https://www.hcl.com/'
    word_list = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code)
    
    for post_text in soup.findAll('span', {'class': 'our-business-title'}):
        content = post_text.string
        print(content)
        words = content.lower().split()
        for each_word in words:
            print("word is "+each_word)
            word_list.append(each_word)
        clean_up_list(word_list)

def clean_up_list(word_list):
    clean_word_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_-+={}[]:;\'<>,./?|"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")
            if len(word) > 0:
                print()
                clean_word_list.append(word)
            create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
    word_count = {}
    for word in clean_word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print("key "+str(key), "value "+str(value))
        
        
start('https://www.hcl.com/')

