# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 10:47:13 2019

@author: SNR
"""

from urllib import request
import requests

goog_url = "https://www.bseindia.com/xml-data/corpfiling/AttachLive/18737abc-49d5-4563-ab9d-c383932202d4.pdf"

def download_stock_data(csv_url):
    #csv_url="https://www.bseindia.com/xml-data/corpfiling/AttachLive/18737abc-49d5-4563-ab9d-c383932202d4.pdf"
    response = request.urlopen(csv_url)
    pdfFile=requests.get(csv_url)
    open('Newspdffile.pdf','wb').write(pdfFile.content)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'NewsPdfFile.pdf'
    fw = open(dest_url, 'w')
    for line in lines:
        fw.write(line + '\n')
    fw.close()
    
download_stock_data(goog_url)