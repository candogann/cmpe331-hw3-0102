"""
Stage : Development -01
@author : Ali Can Doğan , 120200068
@author : Ozan Şentürk , 119200080

"""

from bs4 import BeautifulSoup
import json

with open('./ssd.html', encoding="utf-8") as f:
    soup = BeautifulSoup(f,'html.parser')

tags = soup.find_all('h2')
for i in tags:
    tags = i.find_all(text=True)
    print(tags)