#!/usr/bin/env python3
import os
import sys
import json
import requests
import datetime
import webbrowser
import subprocess

def importAPI():
	global api
	apiraw = requests.get(url='https://r-a-d.io/api', headers={'User-agent': 'Mozilla/5.0'})
	api = apiraw.json()


#def importJson():
#	global data
#	with open(api) as data_file:
#		data = json.load(data_file)


def extractJson():
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


def functionJson():
	global isAfkStreamStr
	if isAfkStream == True:
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
		datetime.timedelta(seconds=songLengthSeconds))

	tempSongLength = readableSongLength[2:3]
	global totalSongTime
	if tempSongLength == 0:
		totalSongTime = readableSongLength[2:7]
	else:
		totalSongTime = readableSongLength[3:7]


def songTimeLeft():
	global currentSongcTimeLeft
	currentSongcTimeLeft = endTime - currentTime

	readableCurrentSongcTimeLeft = str(
		datetime.timedelta(seconds=currentSongcTimeLeft))

	tempCurrentSongcTimeLeft = readableCurrentSongcTimeLeft[2:3]

	if tempCurrentSongcTimeLeft == 0:
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
		datetime.timedelta(seconds=currentSongcTime))

	tempCurrentSongcTime = readableCurrentSongcTime[2:3]

	if tempCurrentSongcTime == 0:
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


def openThread():
	global thread
	if isOldThread == (False):
		if sys.platform == 'darwin':	#osx
			subprocess.Popen(['open', threadUrl])
		else:
			webbrowser.get('firefox').open(threadUrl)
	else:
		print()
		print("Sorry, thread is not up.")
		print()


def start():
	importAPI()

	#importJson()

	extractJson()

	functionJson()

	songTimeLength()

	songTimeLeft()

	songTimeCurrent()

if __name__ == "__main__":
	start()