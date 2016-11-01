from bs4 import BeautifulSoup
import os, sys
import requests


def getAllImages(url):
    #create directory for save images
    os.system("mkdir images")
    
    bs = BeautifulSoup(requests.get(url).text,"html.parser")
    for img in bs.findAll("img"):
        print("found image")
        src = img["src"]
        if src:
            src1 = src
            print(src1)
            r = requests.get(src1,stream=True)
            f = open('images/%s' % src1.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()

getAllImages("http://python.ie/pycon-2016/schedule/")
