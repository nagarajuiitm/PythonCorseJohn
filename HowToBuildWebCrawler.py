# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 12:07:55 2019

@author: SNR
"""
import requests
from bs4 import BeautifulSoup

def BSE_spider(max_pages):
    page = 1
    #max_pages=1
    while page <= max_pages:
        url = "https://www.bseindia.com/corporates/ann.html=" 
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('a', {'class':'ng-binding'}):
            href ="https://www.bseindia.com/corporates" + link.get('href')
            title = link.string
            print(href)
            print(title)
        page += 1
        
def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for item_name in soup.findAll('td', {'class':'tdcolumn ng-binding'}):
        print(item_name.string)
    for link in soup.findAll('a'): 
        href = "https://www.bseindia.com/corporates" + link.get('href')
        print(href)
        
        
    
            
BSE_spider(1)