#!/usr/bin/env python3
import os
import webbrowser
from requests import get
from sys import platform
from subprocess import Popen
from datetime import timedelta

def getJson():
	apiraw = get(url='https://r-a-d.io/api', headers={'User-agent': 'Mozilla/5.0'})
	global api
	api = apiraw.json()

def readJson():
	global djName
	djName = api['main']['dj']['djname']

	global djImage
	djImage = api['main']['dj']['djimage']

	global djDescription
	djDescription = api['main']['dj']['djtext']

	global isAfkStream
	isAfkStream = api['main']['isafkstream']

	global threadUrl
	threadUrl = api['main']['thread']

	global listeners
	listeners = api['main']['listeners']

	global songTitle
	songTitle = api['main']['np']

	global requesting
	requesting = api['main']['requesting']

	global startTime
	startTime = api['main']['start_time']

	global endTime
	endTime = api['main']['end_time']

	global currentTime
	currentTime = api['main']['current']

def readQueue():
	dir_path = os.path.dirname(os.path.realpath(__file__))
	os.environ['dirpath'] = dir_path
	os.system('cd $dirpath && python3 getqueue.py')

def functionJson():
	global isAfkStreamStr
	if isAfkStream == (True):
		isAfkStreamStr = ("AFK Stream")
	else:
		isAfkStreamStr = ("")

	global isOldThread
	if threadUrl != (""):
		if djName == ("Hanyuu-sama"):
			isOldThread = (True)
		else:
			isOldThread = (False)

def songTimeLength():
	global songLengthSeconds
	songLengthSeconds = (endTime - startTime)

	readableSongLength = str(
		timedelta(seconds=songLengthSeconds))

	tempSongLength = readableSongLength[2:3]
	global totalSongTime
	if tempSongLength == (0):
		totalSongTime = readableSongLength[2:7]
	else:
		totalSongTime = readableSongLength[3:7]

def songTimeLeft():
	global currentSongcTimeLeft
	currentSongcTimeLeft = endTime - currentTime

	readableCurrentSongcTimeLeft = str(
		timedelta(seconds=currentSongcTimeLeft))

	tempCurrentSongcTimeLeft = readableCurrentSongcTimeLeft[2:3]

	if tempCurrentSongcTimeLeft == (0):
		formattedCurrentSongcTimeLeft = readableCurrentSongcTimeLeft[2:7]
	else:
		formattedCurrentSongcTimeLeft = readableCurrentSongcTimeLeft[3:7]

	formattedCurrentSongcTimeLeft = ("%s/%s") % (
		formattedCurrentSongcTimeLeft, totalSongTime)

	global currentSongTimeLeft
	currentSongTimeLeft = formattedCurrentSongcTimeLeft

def songTimeCurrent():
	global currentSongcTime
	currentSongcTime = (songLengthSeconds - currentSongcTimeLeft)

	readableCurrentSongcTime = str(
		timedelta(seconds=currentSongcTime))

	tempCurrentSongcTime = readableCurrentSongcTime[2:3]

	if tempCurrentSongcTime == (0):
		formattedCurrentSongcTime = readableCurrentSongcTime[2:7]
	else:
		formattedCurrentSongcTime = readableCurrentSongcTime[3:7]

	formattedCurrentSongcTime = ("%s/%s") % (
		formattedCurrentSongcTime, totalSongTime)

	global currentSongTime
	currentSongTime = formattedCurrentSongcTime
	
	# totalSongTime is song length
	# currentSongTime is how far in the song
	# currentSongTimeLeft is how much time is left

	print(songTitle)
	print(totalSongTime)
	print(currentSongTime)
	print(currentSongTimeLeft)

def openThread():
	global thread
	if isOldThread == (False):
		if platform == ('darwin'):	#osx
			Popen(['open', threadUrl])
		else:
			webbrowser.get('firefox').open(threadUrl)
	else:
		print()
		print("Sorry, thread is not up.")
		print()

def start():
	getJson()

	readJson()

	functionJson()

	songTimeLength()

	songTimeLeft()

	songTimeCurrent()

if __name__ == ("__main__"):
	start()