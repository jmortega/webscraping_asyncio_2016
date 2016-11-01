#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests


r  = requests.get("http://python.ie/pycon-2016/schedule/")

data = r.text

soup = BeautifulSoup(data,"html.parser")

for link in soup.find_all('a'):
    print(link.get('href'))