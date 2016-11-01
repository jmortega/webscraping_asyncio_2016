#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from os import path
from sys import stdout
import codecs
from bs4 import BeautifulSoup
import requests


streamWriter = codecs.lookup('utf-8')[-1]
stdout = streamWriter(stdout)

# a place to store the links we find
links = []

r = requests.get('http://python.ie/pycon-2016/schedule/')
page = r.text
soup = BeautifulSoup(page,"html.parser")
for link in soup.findAll('a', href=True):
    # skip useless links
    if link['href'] == '' or link['href'].startswith('#'):
        continue
    # initialize the link
    thisLink = {
        'url': link['href'],
        'title': link.string,
        'image': '',
    }
    # see if the link contains an image
    img = link.find('img', src=True)
    if img:
        thisLink['image'] = img['src']
        if thisLink['title'] is None:
            # look for a title here if none exists
            if 'title' in img:
                thisLink['title'] = img['title']
            elif 'alt' in img:
                thisLink['title'] = img['alt']
            else:
                thisLink['title'] = path.basename(img['src'])

    if thisLink['title'] is None:
        # check for text inside the link
        if len(link.contents):
            thisLink['title'] = ' '.join(link.stripped_strings)
    if thisLink['title'] is None:
        # if there's *still* no title (empty tag), skip it
        continue
    # convert to something immutable for storage
    hashableLink = (thisLink['url'].strip(),
                    thisLink['title'].strip(),
                    thisLink['image'].strip())
    # store the result
    if hashableLink not in links:
        links.append(hashableLink)

# print the results
for link in links:
    print('\t'.join(link) + '\n')