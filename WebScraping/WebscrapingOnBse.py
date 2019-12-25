# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 09:39:25 2019

@author: SNR
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

def GetNewsDetailsFromBSEWebPage():
    driver = webdriver.Chrome('N:\GitHub\PythonCorseJohn\WebScraping\chromedriver')
    driver.get('https://www.bseindia.com/corporates/ann.html') 
    
    content = driver.page_source
    soup = BeautifulSoup(content,'lxml')
    
    #allNewsData=driver.find_element_by_xpath("//*[@id=\"lblann\"]/table/tbody/tr[4]/td")
    
    newsTable=soup.find_all('td', {'id':'lblann'})
    #print(newsTable[0])
    for news in newsTable:
        details=news.find_all('table',{'class','ng-scope'})
        print(details[0])
        newsString=details.find_all('a',{'class':'ng-binding'})
        newsTime=details.find_all('b',{'class':'ng-binding'})
        print("News:"+str(newsString))
        print("Time of update :"+str(newsTime))
    
    for tableName in rows:
        print(tableName.text)
    for a in soup.findAll('div',href=True, attrs={'id':'lblann'}):
        #a[0]
        name=a.find('class', attrs={'class':'ng-binding'})
        print(name.text)
