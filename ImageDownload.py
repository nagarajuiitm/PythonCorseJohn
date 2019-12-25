# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:25:01 2019

@author: SNR
"""

import urllib.request

def download_web_image(url):
    full_name = "Ramacharan.jpg"
    urllib.request.urlretrieve(url, full_name)
    
download_web_image("http://reedmirchi.com/wp-content/uploads/2017/03/Ram-Charan-Teja-Pictures-Gallery.jpg")