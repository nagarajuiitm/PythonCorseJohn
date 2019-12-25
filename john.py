# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 16:02:46 2019

@author: SNR
"""

import requests
from bs4 import BeautifulSoup

def bse_announcements(csv_url):
    csv_url = 'https://www.bseindia.com/corporates/ann.html'
    source_code = requests.get(csv_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, 'features="lxml"')
    for link in soup.findAll('a', {'class':'ng-binding'}):
        href = 'https://www.bseindia.com/corporates/ann.html'
        print(href)
        
bse_announcements('https://www.bseindia.com/corporates/ann.html')