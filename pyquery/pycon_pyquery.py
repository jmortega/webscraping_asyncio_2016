#!/usr/bin/env python

from pyquery import *
import json
import csv
import sys
import codecs

#its create an instance of the PyQuery class
html = PyQuery(url='http://d6unce.attendify.io/schedule.html')
talks_pycon = []
speakers_pycon = []
#obtain div where can be found each talk info
for row in html('div.session'):
	PyQueryTalk = PyQuery(row)
	title = PyQueryTalk('h5.session__title').text().encode('utf-8')
	session_time = PyQueryTalk('span.session__time').text().encode('utf-8')
	track = PyQueryTalk('div.tracks__name').text().encode('utf-8')
	id = PyQuery(row).attr('data-link')
	if title is not None:
		talk_pycon ={}
		talk_pycon['title'] = title
		talk_pycon['session_time'] = session_time
		talk_pycon['track'] = track
		talk_pycon['id'] = id
		talks_pycon.append(talk_pycon)
  

#obtain info from talk details
for row in html('div.details'):
	PyQueryTalk = PyQuery(row)
	dataSpeaker = PyQueryTalk('div.uv-shortcard__title').text().encode('utf-8')
	dataSpeaker2 = PyQueryTalk('div.uv-shortcard__subtitle').text().encode('utf-8')
	dataSpeaker3 = PyQueryTalk('div.uv-card__description').text().encode('utf-8')
	dataSpeaker4 = PyQueryTalk('h2.uv-card__title').text().encode('utf-8')
	dataSpeaker5 = PyQueryTalk('div.tracks__name').text().encode('utf-8')
	dataSpeaker6 = PyQueryTalk('span.session__location').text().encode('utf-8')
	dataSpeaker7 = PyQueryTalk('span.session__time').text().encode('utf-8')
	if dataSpeaker is not None and dataSpeaker is not "":
		speaker_pycon ={}
		speaker_pycon['name'] = dataSpeaker
		speaker_pycon['details'] = dataSpeaker2
		speaker_pycon['description'] = dataSpeaker3
		speaker_pycon['talk'] = dataSpeaker4
		speaker_pycon['track'] = dataSpeaker5
		speaker_pycon['location'] = dataSpeaker6
		speaker_pycon['time'] = dataSpeaker7
		speakers_pycon.append(speaker_pycon)	
	
with open('pycon_conferences.json','w') as outfile:
        json.dump(talks_pycon,outfile,indent=4)
	
with open('pycon_speakers.json','w') as outfile:
	json.dump(speakers_pycon,outfile,indent=4)