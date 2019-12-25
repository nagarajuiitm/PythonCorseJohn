# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:59:42 2019

@author: SNR
"""

#https://www.tutorialspoint.com/python_web_scraping/

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def GetProductDetailsFromFlipkartPage():
    driver = webdriver.Chrome('N:\GitHub\PythonCorseJohn\WebScraping\chromedriver')
    
    Names = []
    Prices = []
    Ratings = []
    driver.get("https://www.flipkart.com/laptops/</a>~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniq") 
    
    content = driver.page_source
    soup = BeautifulSoup(content)
    allclasses=soup.findAll('a',href=True, attrs={'class':'_31qSD5'})
    for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
        #a[0]
        name=a.find('div', attrs={'class':'_3wU53n'})
        price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
        #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})

        Names.append(name.text)
        Prices.append(price.text)
        #Ratings.append(rating)
        
        df = pd.DataFrame({'Names':name.text, 'Prices':price.text})
    
    csv = df.to_csv('products.csv', index=False, encoding='UTF-8')
    print(csv)

GetProductDetailsFromFlipkartPage()

