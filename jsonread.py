#!/usr/bin/env python3
import json
import urllib.request
from time import sleep

def clearScreen():
	print ("\n" * 200)

clearScreen()

def importJson():
	#data = json.loads(open('test.json').read())
	
	#urllib user agent
	#req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	global data
	with urllib.request.urlopen("https://r-a-d.io/api") as data_file:
		data = json.loads(url.read().decode(), headers={'User-Agent': 'Mozilla/5.0'})

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

	global isAfkStreamStr
	if isAfkStream == True:
		isAfkStreamStr = "AFK Stream"
	else:
		isAfkStreamStr = ""

clearScreen()