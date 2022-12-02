"""
Stage : Development -01
@author : Ali Can Doğan , 120200068
@author : Ozan Şentürk , 119200080

"""

from bs4 import BeautifulSoup
import requests


# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url='https://www.nytimes.com/section/science'
response=requests.get(url,headers=headers)
soup = BeautifulSoup(response.text,'html.parser')

tags = soup.find_all('h2')
for i in tags:
    tags = i.find_all(text=True)
    print(tags)