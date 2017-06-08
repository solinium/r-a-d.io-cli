#!/usr/bin/env python3
import json

def importJson():
	global data
	with open('api.json') as data_file:    
		data = json.load(data_file)

def extractJson():
	global djName
	djName = data['main']['dj']['djname']

	global djImage
	djImage = data['main']['dj']['djimage']

	global djDescription
	djDescription = data['main']['dj']['djtext']

	global isAfkStream
	isAfkStream = data['main']['isafkstream']

	global threadUrl
	threadUrl = data['main']['thread']

	global listeners
	listeners = data['main']['listeners']

	global songTitle
	songTitle = data['main']['np']

	global requesting
	requesting = data['main']['requesting']

	global startTime
	startTime = data['main']['start_time']

	global endTime
	endTime = data['main']['end_time']

	global currentTime
	currentTime = data['main']['current']


	def jsonFunctions():
		global isAfkStreamStr
		if isAfkStream == True:
			isAfkStreamStr = "AFK Stream"
		else:
			isAfkStreamStr = ""

		global isThreadUp
		if threadUrl == (""):
			isThreadUp = (False)
		else:
			if djName == ("Hanyuu-sama"):
				isThreadUp = (False)
			else:
				isThreadUp = (True)