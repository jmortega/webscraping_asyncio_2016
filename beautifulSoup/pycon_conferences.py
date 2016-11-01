#!/usr/bin/env python

from bs4 import BeautifulSoup
import string
import requests
import csv
import json
import codecs


url = "http://d6unce.attendify.io/schedule.html"

talks_pycon = []
data = requests.get(url)
bs = BeautifulSoup(data.text,"html5lib")

talks = bs.find_all('div', {'class': 'session session--minified session--tf12'})

for talk in talks:
	title = talk.find('h5', {'class': 'session__title'})
	session_time = talk.find('span', {'class': 'session__time'})
	track = talk.find('div', {'class': 'tracks__name'})
	attrs = talk.find('div').attrs
	for key in attrs:
		if(key=='data-link'):
			id=attrs[key]

	dataSpeaker = bs.find('div', {"id":id,'class': 'details uv-card__mask'})
	dataSpeaker1 = dataSpeaker.find('div', {'class': 'uv-shortcard__title'})
	dataSpeaker2 = dataSpeaker.find('div', {'class': 'uv-shortcard__subtitle'})
	dataSpeaker3 = dataSpeaker.find('div', {'class': 'uv-card__description'})
	dataSpeaker4 = dataSpeaker.find('h2', {'class': 'uv-card__title'})
	dataSpeaker5 = dataSpeaker.find('div', {'class': 'tracks__name'})
	dataSpeaker6 = dataSpeaker.find('span', {'class': 'session__location'})
	dataSpeaker7 = dataSpeaker.find('span', {'class': 'session__time'})

	talk_pycon = {}
	talk_pycon['title'] = title.getText().encode('ascii', 'ignore').decode('utf-8')
	talk_pycon['session_time'] = dataSpeaker7.getText().encode('ascii', 'ignore').decode('utf-8').strip()
	
	if dataSpeaker6 is not None:
		talk_pycon['session_location'] = dataSpeaker6.getText().encode('ascii', 'ignore').decode('utf-8')
	else:
		talk_pycon['session_location'] = 'None'
		
	if dataSpeaker3 is not None:
		talk_pycon['description'] = dataSpeaker3.getText().encode('ascii', 'ignore').decode('utf-8').strip()
	else:
		talk_pycon['description'] = 'None'	
	
	if dataSpeaker2 is not None:
		talk_pycon['details'] = dataSpeaker2.getText().encode('ascii', 'ignore').decode('utf-8')
	else:
		talk_pycon['details'] = 'None'	

	if track is not None:
		talk_pycon['track'] = track.getText().encode('ascii', 'ignore').decode('utf-8')
	else:
		talk_pycon['track']='None'
	
	if dataSpeaker1 is not None:    
		talk_pycon['speaker'] = dataSpeaker1.getText().encode('ascii', 'ignore').decode('utf-8')
	else:
		talk_pycon['speaker']='None'
	
	talks_pycon.append(talk_pycon)

	
with open('pycon_conferences.json','w') as outfile:
        json.dump(talks_pycon,outfile,indent=4)