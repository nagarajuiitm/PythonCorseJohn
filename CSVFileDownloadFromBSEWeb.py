# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 08:59:42 2019

@author: SNR
"""

from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import pandas as pd

driver = webdriver.chrome('N:\GitHub\PythonCorseJohn')

DateAndTime = []
News = []
TypeOfNews = []
driver.get('https://www.bseindia.com/corporates/ann.html') 

content = driver.page_sourcre
soup = BeautifulSoup(content)
for a in soup.findAll('a', href=True, attrs={"class":"ng-binding"}):
 date =a.find('b', attrs={'class':'ng-binding'})
 news=a.find('a', attrs={'class':'ng-binding'})
 typeofnews =a.find('td', attrs={'class':'tdcolumngrey ng-binding'})
 a = DateAndTime.append(date.text)
 b = News.append(news.text)
 c = TypeOfNews.append(typeofnews)
 print(a)
 print(b)
 print(c)

